const fs = require('fs');

let path = 'second-brain-ai/frontend/src/pages/App.tsx';
let code = fs.readFileSync(path, 'utf8');

// Fix Sidebar visibility
// Old: ${activePage === 'notes' && selectedNoteId ? 'hidden lg:block' : 'block'} 
// New: ${activePage === 'notes' && !selectedNoteId ? 'block' : 'hidden'} lg:block
code = code.replace(
    /\$\{activePage === 'notes' && selectedNoteId \? 'hidden lg:block' : 'block'\}/g,
    "${activePage === 'notes' && !selectedNoteId ? 'block' : 'hidden lg:block'}"
);

// Fix Content Area visibility
// Old: ${activePage === 'notes' && selectedNoteId ? 'block' : 'hidden lg:block'}
// New: ${activePage !== 'notes' || selectedNoteId ? 'block' : 'hidden lg:block'}
code = code.replace(
    /\$\{activePage === 'notes' && selectedNoteId \? 'block' : 'hidden lg:block'\}/g,
    "${activePage !== 'notes' || selectedNoteId ? 'block' : 'hidden lg:block'}"
);

fs.writeFileSync(path, code);
