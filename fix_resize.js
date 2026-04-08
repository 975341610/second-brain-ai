const fs = require('fs');
let code = fs.readFileSync('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/MediaNodeView.tsx', 'utf8');

// 1. Revert the Polaroid Container condition back to original
code = code.replace(
  /kind === 'image' \|\| kind === 'video' \|\| kind === 'audio'/,
  "kind === 'image' || kind === 'video'"
);

// 2. Revert the resize handle wrapper
const targetResize = `{kind !== 'audio' && (
          <div 
            className="absolute bottom-2 right-2 z-30 opacity-0 group-hover/media:opacity-100 transition-opacity duration-200" 
            contentEditable={false}
          >
            <button 
              className="w-5 h-5 flex items-center justify-center cursor-nwse-resize text-stone-400 hover:text-blue-500 transition-colors" 
              type="button" 
              onMouseDown={startResize}
              title="调整大小"
            >
              <div className="w-2.5 h-2.5 border-r-2 border-b-2 border-current rounded-[1px]" />
            </button>
          </div>
        )}`;

const replaceResize = `<div 
          className="absolute bottom-2 right-2 z-30 opacity-0 group-hover/media:opacity-100 transition-opacity duration-200" 
          contentEditable={false}
        >
          <button 
            className="w-5 h-5 flex items-center justify-center cursor-nwse-resize text-stone-400 hover:text-blue-500 transition-colors" 
            type="button" 
            onMouseDown={startResize}
            title="调整大小"
          >
            <div className="w-2.5 h-2.5 border-r-2 border-b-2 border-current rounded-[1px]" />
          </button>
        </div>`;

code = code.replace(targetResize, replaceResize);

fs.writeFileSync('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/MediaNodeView.tsx', code);
console.log("Done");
