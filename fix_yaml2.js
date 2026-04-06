const fs = require('fs');
const pkgPath = 'clean_repo/package.json';
let pkg = fs.readFileSync(pkgPath, 'utf8');

pkg = pkg.replace(/"build:win": "electron-vite build && node scripts\/copy_frontend\.js && electron-builder --win"/, '"build:win": "electron-vite build && node scripts/copy_frontend.js && electron-builder --win"');

// Actually wait, what if `electron-builder` requires an icon and it fails?
// We had an error log locally earlier:
//   • default Electron icon is used  reason=application icon is not set
// So it uses default.

// Is it `cd frontend` in the YAML? In PowerShell (Windows Actions), `cd` modifies the current directory for the whole run block? No, it works like normal shell.
// Let's change the YAML to run the frontend build from root:
const ymlPath = 'clean_repo/.github/workflows/build.yml';
let yml = fs.readFileSync(ymlPath, 'utf8');
yml = yml.replace(/run: \|\n          cd frontend\n          npm install\n          npm run build/, 'run: npm install && npm run build\n        working-directory: ./frontend');
fs.writeFileSync(ymlPath, yml);
