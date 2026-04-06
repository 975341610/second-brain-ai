import * as fs from 'fs';

const indexPath = 'clean_repo/src/main/index.ts';
let indexCode = fs.readFileSync(indexPath, 'utf-8');

// Fix window-close to actually quit
indexCode = indexCode.replace(
  /ipcMain\.on\('window-close', \(\) => \{ if \(mainWindow && !mainWindow\.isDestroyed\(\)\) mainWindow\.hide\(\) \}\);/,
  "ipcMain.on('window-close', () => { app.quit(); });"
);

// Fix window-all-closed to quit on Windows
indexCode = indexCode.replace(
  /app\.on\('window-all-closed', \(\) => \{\s+if \(process\.platform !== 'darwin'\) \{\s+\/\/ 这里我们保持后台运行，驻留托盘\s+\}\s+\}\);/,
  `app.on('window-all-closed', () => {\n  if (process.platform !== 'darwin') {\n    app.quit();\n  }\n});`
);

fs.writeFileSync(indexPath, indexCode, 'utf-8');

const sidecarPath = 'clean_repo/src/main/sidecar.ts';
let sidecarCode = fs.readFileSync(sidecarPath, 'utf-8');

// Use tree-kill to force kill
const newStop = `
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
`;

sidecarCode = sidecarCode.replace(/async stop\(\): Promise<void> \{[\s\S]*?this\.process = null;\n    \}\n  \}/, newStop.trim());
fs.writeFileSync(sidecarPath, sidecarCode, 'utf-8');

console.log('Fixed close and kill behaviors');
