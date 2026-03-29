
const fs = require('fs');
const path = require('path');

function copyDir(src, dest) {
    fs.mkdirSync(dest, { recursive: true });
    let entries = fs.readdirSync(src, { withFileTypes: true });

    for (let entry of entries) {
        let srcPath = path.join(src, entry.name);
        let destPath = path.join(dest, entry.name);

        if (entry.isDirectory()) {
            copyDir(srcPath, destPath);
        } else {
            fs.copyFileSync(srcPath, destPath);
        }
    }
}

const srcDir = path.join(__dirname, '../frontend/dist');
const destDir = path.join(__dirname, '../out/renderer');

console.log('Copying frontend build to out/renderer...');
if (fs.existsSync(srcDir)) {
    copyDir(srcDir, destDir);
    // Also need to ensure splash.html is there since it's used by main process
    const splashSrc = path.join(__dirname, '../src/renderer/splash.html');
    const splashDest = path.join(destDir, 'splash.html');
    if (fs.existsSync(splashSrc)) {
        fs.copyFileSync(splashSrc, splashDest);
    }
    console.log('Copy completed.');
} else {
    console.error('Frontend dist not found!');
    process.exit(1);
}
