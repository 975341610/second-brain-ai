const fs = require('fs');
const path = require('path');
console.log('Testing frontend copy script in local...');
try {
    require('./clean_repo/scripts/copy_frontend.js');
} catch (e) {
    console.error(e);
}
