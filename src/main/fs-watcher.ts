import { watch, watchFile, unwatchFile, Stats, readFileSync } from 'fs';
import { BrowserWindow } from 'electron';
import path from 'path';

/**
 * 极简 SSOT 文件系统监听器 (原生 Node.js 实现)
 * 监听指定目录下的笔记变更，并通过 IPC 推送到渲染进程。
 */
export class SSOTWatcher {
  private notesDir: string;
  private mainWindow: BrowserWindow;
  private activeWatchers: Map<string, any> = new Map();

  constructor(notesDir: string, mainWindow: BrowserWindow) {
    this.notesDir = notesDir;
    this.mainWindow = mainWindow;
  }

  /**
   * 监听整个笔记目录 (递归)
   */
  public watchAll() {
    console.log(`[SSOT] Starting FS watcher for: ${this.notesDir}`);
    
    try {
      const watcher = watch(this.notesDir, { recursive: true }, (eventType, filename) => {
        if (filename && filename.endsWith('.md')) {
          console.log(`[SSOT] File change detected: ${filename} (${eventType})`);
          this.notifyRenderer(filename, eventType);
        }
      });
      
      this.activeWatchers.set('root', watcher);
    } catch (err) {
      console.error(`[SSOT] Failed to start watcher:`, err);
    }
  }

  /**
   * 针对特定笔记文件的精细监听 (使用 watchFile 以获得更高的跨平台稳定性)
   */
  public watchNote(noteId: number, filePath: string) {
    const absolutePath = path.isAbsolute(filePath) 
      ? filePath 
      : path.join(this.notesDir, filePath);

    // 移除旧的监听 (如果存在)
    this.unwatchNote(noteId);

    console.log(`[SSOT] Watching specific note: ${absolutePath}`);

    watchFile(absolutePath, { interval: 1000 }, (curr: Stats, prev: Stats) => {
      if (curr.mtime !== prev.mtime) {
        console.log(`[SSOT] Note content changed on disk: ${absolutePath}`);
        try {
          // 直接读取内容发送，减少渲染进程的一次读取开销
          const content = readFileSync(absolutePath, 'utf-8');
          this.mainWindow.webContents.send('ssot:note-changed', {
            noteId,
            path: absolutePath,
            content,
            mtime: curr.mtime
          });
        } catch (e) {
          console.error(`[SSOT] Failed to read file content:`, e);
        }
      }
    });

    this.activeWatchers.set(`note-${noteId}`, absolutePath);
  }

  public unwatchNote(noteId: number) {
    const filePath = this.activeWatchers.get(`note-${noteId}`);
    if (filePath) {
      unwatchFile(filePath);
      this.activeWatchers.delete(`note-${noteId}`);
    }
  }

  private notifyRenderer(filename: string, eventType: string) {
    if (this.mainWindow && !this.mainWindow.isDestroyed()) {
      this.mainWindow.webContents.send('ssot:fs-event', {
        filename,
        eventType
      });
    }
  }

  public stopAll() {
    const rootWatcher = this.activeWatchers.get('root');
    if (rootWatcher) rootWatcher.close();
    
    for (const [key, val] of this.activeWatchers.entries()) {
      if (key.startsWith('note-')) {
        unwatchFile(val);
      }
    }
    this.activeWatchers.clear();
  }
}
