const fs = require('fs');
const pkgPath = 'clean_repo/package.json';
let pkg = fs.readFileSync(pkgPath, 'utf8');

pkg = pkg.replace(/"build:win": "npm run build:frontend && electron-vite build && node scripts\/copy_frontend\.js && electron-builder --win"/, '"build:win": "electron-vite build && node scripts/copy_frontend.js && electron-builder --win"');

fs.writeFileSync(pkgPath, pkg);
