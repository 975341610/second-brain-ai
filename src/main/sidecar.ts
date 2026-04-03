import { spawn, ChildProcess } from 'child_process';
import treeKill from 'tree-kill';
import path from 'path';
import log from 'electron-log';

export class SidecarManager {
  private process: ChildProcess | null = null;
  private backendPath: string;
  private isDev: boolean;

  constructor(backendPath: string, isDev: boolean) {
    this.backendPath = backendPath;
    this.isDev = isDev;
    
    // 配置 electron-log
    log.transports.file.level = 'info';
    log.info('SidecarManager initialized with backendPath:', backendPath, 'isDev:', isDev);
  }

  async start(): Promise<void> {
    let command: string;
    let args: string[];

    if (this.isDev) {
      command = process.platform === 'win32' ? 'python' : 'python3';
      args = ['main.py'];
    } else {
      // 生产环境下，执行打包好的 backend 可执行文件
      // 根据 package.json 的 extraResources，它在 process.resourcesPath/backend 目录下
      const exeName = process.platform === 'win32' ? 'backend.exe' : 'backend';
      command = path.join(this.backendPath, exeName);
      args = [];
    }

    log.info(`Starting sidecar process: ${command} ${args.join(' ')}`);
    log.info(`Sidecar working directory: ${this.backendPath}`);

    try {
      this.process = spawn(command, args, {
      cwd: this.backendPath,
      stdio: 'pipe', // 修改为 pipe 以便捕获输出
      shell: false,
      detached: true,
      env: {
        ...process.env,
        PORT: '8765',
        HOST: '127.0.0.1',
        PYTHONUNBUFFERED: '1'
      }
    });

    } catch (err) {
      log.error('Synchronous error during spawn:', err);
      throw err;
    }

    if (this.process.stdout) {
      this.process.stdout.on('data', (data) => {
        const output = data.toString().trim();
        if (output) {
          log.info(`[Backend STDOUT] ${output}`);
        }
      });
    }

    if (this.process.stderr) {
      this.process.stderr.on('data', (data) => {
        const output = data.toString().trim();
        if (output) {
          log.error(`[Backend STDERR] ${output}`);
        }
      });
    }

    // Resolve immediately rather than waiting for python to boot up
    log.info('Backend process spawned, resolving start promise immediately for fast startup');
    return Promise.resolve();
  }

  private async waitForBackendReady(retries = 10): Promise<void> {
    const healthUrl = 'http://127.0.0.1:8765/health'; // 假设后端有 /health 接口
    for (let i = 0; i < retries; i++) {
      try {
        
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 2000);
        const response = await fetch(healthUrl, { signal: controller.signal as any });
        clearTimeout(timeoutId);

        if (response.ok) return;
      } catch (e) {
        // ignore
      }
      await new Promise(resolve => setTimeout(resolve, 1000));
    }
    throw new Error('Backend failed to start after multiple retries');
  }

  async stop(): Promise<void> {
    if (this.process?.pid) {
      log.info('Killing sidecar process using tree-kill...');
      try {
        await new Promise<void>((resolve, reject) => {
          treeKill(this.process!.pid!, 'SIGKILL', (err) => {
            if (err) {
              log.error('tree-kill error:', err);
              reject(err);
            } else {
              log.info('Sidecar process tree killed successfully.');
              resolve();
            }
          });
        });
      } catch (e) {
        log.error('Failed to kill sidecar gracefully, forcing kill...', e);
        this.process.kill('SIGKILL');
      }
      this.process = null;
    }
  }

  isAlive(): boolean {
    return this.process !== null && !this.process.killed;
  }
}
