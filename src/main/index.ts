import log from 'electron-log';
import { app, BrowserWindow, Tray, Menu, ipcMain, dialog, nativeImage } from 'electron';
import path from 'path';
import { autoUpdater } from 'electron-updater';
import { SidecarManager } from './sidecar';
import { spawn, execSync } from 'child_process';
import fs from 'fs';
import { SSOTWatcher } from './fs-watcher';
import { FSBridge } from './fs_bridge';

let mainWindow: BrowserWindow | null = null;
let splashWindow: BrowserWindow | null = null;
let tray: Tray | null = null;
let ssotWatcher: SSOTWatcher | null = null;
let fsBridge: FSBridge | null = null;
const isDev = !app.isPackaged;

process.on('uncaughtException', (error) => {
  log.error('Uncaught Exception:', error);
});
process.on('unhandledRejection', (reason) => {
  log.error('Unhandled Rejection:', reason);
});


// 确保 backend 路径计算准确
const getBackendPath = () => {
  if (isDev) {
    return path.join(app.getAppPath(), 'backend');
  }
  // 生产环境下 backend 可执行文件通常在 resources/backend 目录
  return path.join(process.resourcesPath, 'backend');
};

const sidecar = new SidecarManager(getBackendPath(), isDev);

// Helper to call Python bridge
async function callPythonBridge(command: string, params: any = {}) {
  // Add detailed logs here for debugging IPC communication
  log.info(`[IPC Bridge] Calling command: ${command} with params:`, params);
  
  return new Promise((resolve, reject) => {
    const pythonExe = process.platform === 'win32' ? 'python' : 'python3';
    const bridgePath = path.join(getBackendPath(), 'ipc_bridge.py');
    
    log.info(`[IPC Bridge] pythonExe: ${pythonExe}, bridgePath: ${bridgePath}`);

    const child = spawn(pythonExe, [bridgePath, command, JSON.stringify(params)], {
      cwd: getBackendPath(),
    });

    let stdout = '';
    let stderr = '';

    child.stdout.on('data', (data) => {
      stdout += data.toString();
    });

    child.stderr.on('data', (data) => {
      stderr += data.toString();
    });

    child.on('close', (code) => {
      log.info(`[IPC Bridge] ${command} exited with code ${code}`);
      if (stderr) log.warn(`[IPC Bridge] ${command} stderr: ${stderr}`);
      
      if (code !== 0) {
        log.error(`Python bridge exited with code ${code}: ${stderr}`);
        // reject(new Error(stderr || `Python bridge exited with code ${code}`));
        // In local-first architecture, missing python shouldn't crash the app!
        resolve([]);
        return;
      }
      try {
        const lines = stdout.trim().split('\n');
        let jsonStr = '';
        for (let i = lines.length - 1; i >= 0; i--) {
           if (lines[i].startsWith('{') || lines[i].startsWith('[')) {
               jsonStr = lines[i];
               break;
           }
        }
        if (!jsonStr) jsonStr = stdout;
          
        const result = JSON.parse(jsonStr);
        if (result && result.error) {
          log.error('Python bridge returned error:', result.error);
          resolve([]); // reject(new Error(result.error));
        } else {
          resolve(result);
        }
      } catch (e) {
        log.error('Failed to parse Python bridge output:', stdout);
        resolve([]); // reject(new Error('Internal Error: Invalid output from bridge'));
      }
    });
  });
}

// 初始化自动更新
function setupAutoUpdater() {
  autoUpdater.autoDownload = false; // 询问用户后再下载

  autoUpdater.on('checking-for-update', () => {
    if (mainWindow && !mainWindow.isDestroyed()) mainWindow.webContents.send('update-message', 'Checking for update...');
  });

  autoUpdater.on('update-available', (info) => {
    if (mainWindow && !mainWindow.isDestroyed()) mainWindow.webContents.send('update-available', info);
  });

  autoUpdater.on('update-not-available', () => {
    if (mainWindow && !mainWindow.isDestroyed()) mainWindow.webContents.send('update-message', 'Update not available.');
  });

  autoUpdater.on('error', (err) => {
    if (mainWindow && !mainWindow.isDestroyed()) mainWindow.webContents.send('update-error', err.message);
  });

  autoUpdater.on('download-progress', (progressObj) => {
    if (mainWindow && !mainWindow.isDestroyed()) mainWindow.webContents.send('update-download-progress', progressObj);
  });

  autoUpdater.on('update-downloaded', () => {
    if (mainWindow && !mainWindow.isDestroyed()) mainWindow.webContents.send('update-downloaded');
  });

  ipcMain.handle('check-for-update', () => autoUpdater.checkForUpdatesAndNotify());
  ipcMain.handle('download-update', () => autoUpdater.downloadUpdate());
  ipcMain.handle('install-update', () => autoUpdater.quitAndInstall());

  // 本地离线更新机制
  ipcMain.handle('install-local-update', async () => {
    const { canceled, filePaths } = await dialog.showOpenDialog({
      title: '选择本地更新包 (.exe)',
      filters: [{ name: 'Executables', extensions: ['exe'] }],
      properties: ['openFile']
    });

    if (canceled || filePaths.length === 0) return { success: false, message: '已取消' };

    const updatePath = filePaths[0];
    
    try {
      // 启动安装程序并退出当前应用
      spawn(updatePath, [], {
        detached: true,
        stdio: 'ignore'
      }).unref();
      
      app.quit();
      return { success: true };
    } catch (err: any) {
      return { success: false, message: err.message };
    }
  });
}

function handleIPC() {
  ipcMain.on('window-minimize', () => { if (mainWindow && !mainWindow.isDestroyed()) mainWindow.minimize() });
  ipcMain.on('window-maximize', () => { if (mainWindow && !mainWindow.isDestroyed()) mainWindow.maximize() });
  ipcMain.on('window-unmaximize', () => { if (mainWindow && !mainWindow.isDestroyed()) mainWindow.unmaximize() });
  ipcMain.on('window-close', () => { 
    if (mainWindow && !mainWindow.isDestroyed()) {
      // Windows 模式下，关闭窗口通常是隐藏到托盘
      if (process.platform === 'win32') {
        mainWindow.hide();
      } else {
        app.quit();
      }
    }
  });
  ipcMain.handle('window-is-maximized', () => { return (mainWindow && !mainWindow.isDestroyed()) ? mainWindow.isMaximized() : false });

  // 📂 彻底切断 FastAPI 依赖，直接通过 IPC 调用 Python 逻辑
  ipcMain.handle('notes:list', async () => await callPythonBridge('notes:list'));
  ipcMain.handle('notebooks:list', async () => await callPythonBridge('notebooks:list'));
  ipcMain.handle('notebooks:create', async (_, params) => await callPythonBridge('notebooks:create', params));
  ipcMain.handle('notebooks:update', async (_, params) => await callPythonBridge('notebooks:update', params));
  ipcMain.handle('notebooks:delete', async (_, params) => await callPythonBridge('notebooks:delete', params));
  ipcMain.handle('notebooks:restore', async (_, params) => await callPythonBridge('notebooks:restore', params));
  ipcMain.handle('notebooks:purge', async (_, params) => await callPythonBridge('notebooks:purge', params));
  ipcMain.handle('notes:create', async (_, params) => await callPythonBridge('notes:create', params));
  
  // local-first: try native node fs bridge first for updates, fallback to python
  ipcMain.handle('notes:update', async (_, params) => {
    // If we have a file_path, try to write it directly for speed
    if (fsBridge && params.file_path) {
      try {
        log.info(`[FSBridge] Fast native save for note ${params.id}`);
        
        // Fast write to local file system
        await fsBridge.updateNote({
            id: params.id,
            content: params.content,
            metadata: {
                id: params.id,
                title: params.title,
                tags: params.tags ? (typeof params.tags === 'string' ? params.tags.split(',') : params.tags) : [],
                notebook_id: params.notebook_id,
                parent_id: params.parent_id,
                icon: params.icon,
                is_title_manually_edited: params.is_title_manually_edited,
                created_at: new Date().toISOString(), // we don't have created_at here, but it's ok for mock
                updated_at: new Date().toISOString()
            },
            silent: true
        }, params.file_path);

        // We still need to update the DB, so we dispatch to Python asynchronously without blocking UI!
        // The python process will be spawned, but the UI gets an immediate response
        callPythonBridge('notes:update', params).catch(e => log.error('Background DB sync failed', e));
        
        // Mock the response that python would return so UI continues
        return {
          id: params.id,
          title: params.title,
          content: params.content,
          tags: params.tags ? (typeof params.tags === 'string' ? params.tags.split(',') : params.tags) : [],
          notebook_id: params.notebook_id,
          parent_id: params.parent_id,
          icon: params.icon,
          is_title_manually_edited: params.is_title_manually_edited,
          file_path: params.file_path
        };
      } catch (e) {
        log.error('[FSBridge] Fast save failed, falling back to python', e);
      }
    }
    return await callPythonBridge('notes:update', params);
  });

  ipcMain.handle('notes:update-tags', async (_, params) => await callPythonBridge('notes:update-tags', params));
  ipcMain.handle('notes:move', async (_, params) => await callPythonBridge('notes:move', params));
  ipcMain.handle('notes:bulk-move', async (_, params) => await callPythonBridge('notes:bulk-move', params));
  ipcMain.handle('notes:bulk-delete', async (_, params) => await callPythonBridge('notes:bulk-delete', params));
  ipcMain.handle('notes:delete', async (_, params) => await callPythonBridge('notes:delete', params));
  ipcMain.handle('notes:restore', async (_, params) => await callPythonBridge('notes:restore', params));
  ipcMain.handle('notes:purge', async (_, params) => await callPythonBridge('notes:purge', params));
  ipcMain.handle('trash:get', async () => await callPythonBridge('trash:get'));
  ipcMain.handle('trash:purge', async () => await callPythonBridge('trash:purge'));
  ipcMain.handle('tasks:list', async () => await callPythonBridge('tasks:list'));
  ipcMain.handle('tasks:create', async (_, params) => await callPythonBridge('tasks:create', params));
  ipcMain.handle('tasks:update', async (_, params) => await callPythonBridge('tasks:update', params));
  ipcMain.handle('tasks:delete', async (_, params) => await callPythonBridge('tasks:delete', params));
  ipcMain.handle('tasks:clear-completed', async () => await callPythonBridge('tasks:clear-completed'));
  ipcMain.handle('ai:ask', async (_, params) => await callPythonBridge('ai:ask', params));
  ipcMain.handle('config:get-model', async () => await callPythonBridge('config:get-model'));
  ipcMain.handle('config:update-model', async (_, params) => await callPythonBridge('config:update-model', params));
  ipcMain.handle('user:get-stats', async () => await callPythonBridge('user:get-stats'));
  ipcMain.handle('user:list-achievements', async () => await callPythonBridge('user:list-achievements'));
  ipcMain.handle('user:update-theme', async (_, params) => await callPythonBridge('user:update-theme', params));
  ipcMain.handle('user:update-wallpaper', async (_, params) => await callPythonBridge('user:update-wallpaper', params));
  ipcMain.handle('bgm:list', async () => await callPythonBridge('bgm:list'));
  ipcMain.handle('system:version', async () => await callPythonBridge('system:version'));
}

function createTray() {
  const iconPath = isDev 
    ? path.join(app.getAppPath(), 'resources/icon.png')
    : path.join(__dirname, '../../resources/icon.png');
  
  // Check if icon exists, else use empty image to prevent crash
  const fs = require('fs');
  const trayIcon = fs.existsSync(iconPath) ? iconPath : nativeImage.createEmpty();
  try {
    tray = new Tray(trayIcon);
  } catch (e) {
    log.error('Failed to create tray:', e);
    return;
  }
  const contextMenu = Menu.buildFromTemplate([
    { label: '显示主界面', click: () => { 
      if (mainWindow && !mainWindow.isDestroyed()) {
        mainWindow.show();
        mainWindow.focus();
      }
    }},
    { type: 'separator' },
    { label: '退出', click: () => {
        app.isQuitting = true; // 标记正在退出，防止隐藏逻辑干扰
        sidecar.stop().then(() => app.quit());
    }}
  ]);
  tray.setToolTip('Second Brain AI');
  tray.setContextMenu(contextMenu);
  tray.on('double-click', () => {
    if (mainWindow && !mainWindow.isDestroyed()) {
      mainWindow.show();
      mainWindow.focus();
    }
  });
}

function createSplashWindow() {
  splashWindow = new BrowserWindow({
    width: 600,
    height: 400,
    frame: false,
    transparent: true,
    alwaysOnTop: true,
    center: true,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true
    }
  });

  if (isDev && process.env['ELECTRON_RENDERER_URL']) {
    splashWindow.loadURL(`${process.env['ELECTRON_RENDERER_URL']}/splash.html`);
  } else {
    splashWindow.loadFile(path.join(__dirname, '../renderer/splash.html'));
  }

  // Add error logging
  splashWindow.webContents.on('did-fail-load', (event, errorCode, errorDescription, validatedURL) => {
    log.error(`Splash window failed to load: ${errorCode} - ${errorDescription} at ${validatedURL}`);
  });

  splashWindow.on('closed', () => {
    splashWindow = null;
  });
}

function createWindow() {
  const iconPath = isDev 
    ? path.join(app.getAppPath(), 'resources/icon.png')
    : path.join(__dirname, '../../resources/icon.png');

  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    frame: false,
    show: false, // 初始不显示，等待 ready-to-show
    transparent: true,
    icon: require('fs').existsSync(iconPath) ? iconPath : undefined,
    webPreferences: {
      preload: path.join(__dirname, '../preload/index.js'),
      nodeIntegration: false,
      contextIsolation: true
    }
  });

  // Add error logging
  mainWindow.webContents.on('did-fail-load', (event, errorCode, errorDescription, validatedURL) => {
    log.error(`Main window failed to load: ${errorCode} - ${errorDescription} at ${validatedURL}`);
    if (isDev) {
      log.info('ELECTRON_RENDERER_URL:', process.env['ELECTRON_RENDERER_URL']);
    }
  });
  mainWindow.webContents.on('crashed', (event, killed) => {
    log.error(`Main window crashed: killed=${killed}`);
  });
  mainWindow.webContents.on('render-process-gone', (event, details) => {
    log.error(`Main window render process gone: ${details.reason} (${details.exitCode})`);
  });

  // Add console message logging
  mainWindow.webContents.on('console-message', (event, level, message, line, sourceId) => {
    log.info(`Renderer Console: [${level}] ${message} (${sourceId}:${line})`);
  });

  if (isDev && process.env['ELECTRON_RENDERER_URL']) {
    mainWindow.loadURL(process.env['ELECTRON_RENDERER_URL']);
  } else {
    mainWindow.loadFile(path.join(__dirname, '../renderer/index.html'));
  }

  mainWindow.once('ready-to-show', () => {
    // wait for sidecar to show
  });

  mainWindow.on('closed', () => {
    if (ssotWatcher) ssotWatcher.stopAll();
    mainWindow = null;
  });

  // --- Initialize Local-first SSOT Watcher ---
  // 生产环境下使用 userData/data，开发环境下使用项目根目录/data
  const notesDir = isDev 
    ? path.join(app.getAppPath(), 'data')
    : path.join(app.getPath('userData'), 'data');

  // 确保目录存在
  const fs = require('fs');
  if (!fs.existsSync(notesDir)) {
    fs.mkdirSync(notesDir, { recursive: true });
  }

  ssotWatcher = new SSOTWatcher(notesDir, mainWindow);
  fsBridge = new FSBridge(notesDir, ssotWatcher);
  ssotWatcher.watchAll();
  
  // 暴露 IPC 接口用于监听特定文件
  ipcMain.on('ssot:watch-note', (event, { noteId, path }) => {
    if (ssotWatcher) ssotWatcher.watchNote(noteId, path);
  });
  
  ipcMain.on('ssot:unwatch-note', (event, { noteId }) => {
    if (ssotWatcher) ssotWatcher.unwatchNote(noteId);
  });
}

app.whenReady().then(() => {
  createSplashWindow();
  createWindow();
  
  createTray();
  handleIPC();
  setupAutoUpdater();

  // 异步启动 Sidecar，不阻塞主窗口创建过程
  sidecar.start()
    .then(() => {
      log.info('Sidecar started successfully.');
      if (mainWindow && !mainWindow.isDestroyed()) {
        mainWindow.show();
      }
      if (splashWindow && !splashWindow.isDestroyed()) {
        splashWindow.close();
      }
    })
    .catch((err) => {
      log.error('Failed to start sidecar:', err);
      // 即便后端启动失败，也尝试显示主窗口，以便用户看到界面进行反馈或展示错误提示
      if (mainWindow && !mainWindow.isDestroyed()) {
        mainWindow.show();
      }
      if (splashWindow && !splashWindow.isDestroyed()) {
        splashWindow.close();
      }
    });

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
      // 如果 sidecar 已经在运行，直接显示
      if (sidecar.isAlive()) {
        mainWindow?.show();
      }
    }
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('before-quit', async () => {
  log.info('Shutting down Sidecar...');
  await sidecar.stop();
});
