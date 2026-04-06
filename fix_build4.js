const fs = require('fs');

// Windows `&&` in powershell inside npm run scripts sometimes fails if a warning occurs.
// Let's modify package.json `build:win` to be sequential.
const pkgPath = 'clean_repo/package.json';
let pkg = JSON.parse(fs.readFileSync(pkgPath, 'utf8'));

pkg.scripts['build:win'] = 'npm run build:electron && npm run copy:frontend && npm run build:builder';
pkg.scripts['build:electron'] = 'electron-vite build';
pkg.scripts['copy:frontend'] = 'node scripts/copy_frontend.js';
pkg.scripts['build:builder'] = 'electron-builder --win';

fs.writeFileSync(pkgPath, JSON.stringify(pkg, null, 2));
