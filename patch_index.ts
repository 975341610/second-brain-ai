import * as fs from 'fs';
import * as path from 'path';

const indexPath = 'clean_repo/src/main/index.ts';
let code = fs.readFileSync(indexPath, 'utf-8');

// Add global error handlers at the top
const globalErrorHandlers = `
import log from 'electron-log';
process.on('uncaughtException', (error) => {
  log.error('Uncaught Exception in Main Process:', error);
});
process.on('unhandledRejection', (reason, promise) => {
  log.error('Unhandled Rejection at:', promise, 'reason:', reason);
});
`;

if (!code.includes('uncaughtException')) {
    code = code.replace("import { app,", "import log from 'electron-log';\nimport { app,");
    code = code.replace("const isDev = !app.isPackaged;", "const isDev = !app.isPackaged;\n\nprocess.on('uncaughtException', (error) => {\n  log.error('Uncaught Exception:', error);\n});\nprocess.on('unhandledRejection', (reason) => {\n  log.error('Unhandled Rejection:', reason);\n});\n");
}

// Fix createTray
code = code.replace(/tray = new Tray\(iconPath\);/, `import { nativeImage } from 'electron';\n  // Check if icon exists, else use empty image to prevent crash\n  const fs = require('fs');\n  const trayIcon = fs.existsSync(iconPath) ? iconPath : nativeImage.createEmpty();\n  try {\n    tray = new Tray(trayIcon);\n  } catch (e) {\n    log.error('Failed to create tray:', e);\n    return;\n  }`);

// Fix createWindow icon
code = code.replace(/icon: iconPath,/g, `icon: require('fs').existsSync(iconPath) ? iconPath : undefined,`);

fs.writeFileSync(indexPath, code, 'utf-8');
console.log('patched index.ts');
