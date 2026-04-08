const fs = require('fs');
let code = fs.readFileSync('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/MediaNodeView.tsx', 'utf8');

// For Audio, we want to NOT render the floating toolbar (GripVertical & Trash2) because the user wants to rely on the global block handle.
// The floating toolbar is currently rendered inside the <div className="absolute top-3 right-3 z-30...

const targetToolbarStart = '<div \n          className="absolute top-3 right-3 z-30 flex items-center gap-1.5 opacity-0 group-hover/media:opacity-100 transition-opacity duration-200" \n          contentEditable={false}\n        >';
const replaceToolbarStart = `{kind !== 'audio' && (<div \n          className="absolute top-3 right-3 z-30 flex items-center gap-1.5 opacity-0 group-hover/media:opacity-100 transition-opacity duration-200" \n          contentEditable={false}\n        >`;

code = code.replace(targetToolbarStart, replaceToolbarStart);

// We need to find the end of the floating toolbar block
// The block ends right before {/* Content */}

const targetToolbarEnd = `</button>\n          </div>\n        </div>\n\n        {/* Content */}`;
const replaceToolbarEnd = `</button>\n          </div>\n        </div>)}\n\n        {/* Content */}`;
code = code.replace(targetToolbarEnd, replaceToolbarEnd);

fs.writeFileSync('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/MediaNodeView.tsx', code);
console.log("Done");
