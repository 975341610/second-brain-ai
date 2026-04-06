import * as fs from 'fs';

const indexPath = 'clean_repo/src/main/index.ts';
let code = fs.readFileSync(indexPath, 'utf-8');

// Fix the import nativeImage inside function error
code = code.replace(/import \{ nativeImage \} from 'electron';/, '');
code = code.replace(/import \{ app, BrowserWindow, Tray, Menu, ipcMain, dialog \}/, "import { app, BrowserWindow, Tray, Menu, ipcMain, dialog, nativeImage }");

fs.writeFileSync(indexPath, code, 'utf-8');
console.log('fixed import error');
