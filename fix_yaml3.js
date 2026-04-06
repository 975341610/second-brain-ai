const fs = require('fs');

const ymlPath = 'clean_repo/.github/workflows/build.yml';
let yml = fs.readFileSync(ymlPath, 'utf8');

yml = yml.replace(/npm run build\n          cd \.\./, "npm run build");

fs.writeFileSync(ymlPath, yml);
