const fs = require('fs');
const ymlPath = 'clean_repo/.github/workflows/build.yml';
let yml = fs.readFileSync(ymlPath, 'utf8');

// If CI is true, vite treats warnings as errors sometimes, or memory limit hits.
// Let's modify package.json instead to increase memory limit and ignore typescript errors for now if that's the cause.
// In the user's message, "github上全都打包失败了呀", this means the GitHub Action failed.
// Why did it fail? In my local test, `npm run build:frontend` took 4 seconds, then `electron-builder` failed because of `wine` (expected on linux). 
// But on Windows it shouldn't need wine.
// Did the frontend build fail on GitHub Actions because of TypeScript errors?
