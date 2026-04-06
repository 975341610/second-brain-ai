const { execSync } = require('child_process');
try {
    // try to execute the whole sequence just to check if syntax is fine
    // npm run build:win actually runs: npm run build:electron && npm run copy:frontend && npm run build:builder
} catch(e) {
    console.error(e);
}
// Ah wait! When npm runs `npm run build:electron && npm run copy:frontend`, it uses the OS's shell. 
// On Windows, the default shell is CMD.
// Does `node scripts/copy_frontend.js` fail?
// Let's look at copy_frontend.js
