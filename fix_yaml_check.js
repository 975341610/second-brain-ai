const fs = require('fs');

// We have build.yml
// 1. Build Python Backend
// 2. Build React Frontend (working directory ./frontend)
// 3. Install Dependencies (root)
// 4. Build Windows App (npm run build:win)
// 
// If it fails on Build Windows App, it's either `electron-vite build`, `node scripts/copy_frontend.js`, or `electron-builder --win`.
// Let's modify build.yml to run them step by step so we know EXACTLY which one fails!

const ymlPath = 'clean_repo/.github/workflows/build.yml';
let yml = fs.readFileSync(ymlPath, 'utf8');

yml = yml.replace(/run: npm run build:win/, `run: |
          npm run build:electron
          npm run copy:frontend
          npm run build:builder`);

fs.writeFileSync(ymlPath, yml);
