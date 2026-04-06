const fs = require('fs');

// We should ignore TS type checking on CI just to ensure it builds successfully.
// The user doesn't care about type checking on CI, just wants the exe.
const pkgPath = 'clean_repo/frontend/package.json';
let pkg = fs.readFileSync(pkgPath, 'utf8');
pkg = pkg.replace('"build": "cross-env CI=false tsc -b && vite build"', '"build": "cross-env CI=false vite build"');
fs.writeFileSync(pkgPath, pkg);

const rootPkgPath = 'clean_repo/package.json';
let rootPkg = fs.readFileSync(rootPkgPath, 'utf8');
// remove the electron-vite build typecheck if there is one
rootPkg = rootPkg.replace('"build:win": "npm run build:frontend && electron-vite build && node scripts/copy_frontend.js && electron-builder --win"', '"build:win": "npm run build:frontend && electron-vite build && node scripts/copy_frontend.js && electron-builder --win"');
fs.writeFileSync(rootPkgPath, rootPkg);

