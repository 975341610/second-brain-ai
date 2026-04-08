const fs = require('fs');

let code = fs.readFileSync('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/widgets/KanbanComponent.tsx', 'utf8');

// 1. Add GripHorizontal and Trash2 to imports
code = code.replace(
  "import { Plus, ChevronLeft, ChevronRight, CheckCircle2, Circle } from 'lucide-react';",
  "import { Plus, ChevronLeft, ChevronRight, CheckCircle2, Circle, GripHorizontal, Trash2 } from 'lucide-react';"
);

// 2. Add group and relative to NodeViewWrapper, remove data-drag-handle
code = code.replace(
  /<NodeViewWrapper \n      className={`my-6 rounded-2xl border \${morandi.border} \${morandi.bg} shadow-sm shadow-black\/5 hover:shadow-md hover:-translate-y-1 transition-all overflow-hidden select-none \${selected \? 'ring-2 ring-black\/10' : ''}`}\n      data-drag-handle\n    >/,
  '<NodeViewWrapper \n      className={`group relative my-6 rounded-2xl border ${morandi.border} ${morandi.bg} shadow-sm shadow-black/5 hover:shadow-md hover:-translate-y-1 transition-all overflow-hidden select-none ${selected ? \'ring-2 ring-black/10\' : \'\'}`}\n    >'
);

// 3. Add drag and delete buttons when selected
const floatingMenu = `
      {selected && (
        <div className="absolute top-3 right-3 z-50 flex gap-0.5 opacity-0 group-hover:opacity-100 transition-opacity duration-200">
          <div className="flex items-center bg-white/90 backdrop-blur-md border border-[#E6DFD8] rounded-lg shadow-sm overflow-hidden text-[#6E6868]">
            <button 
              className="p-1.5 hover:bg-[#F6F3EF] hover:text-[#3F3A3A] cursor-grab active:cursor-grabbing transition-colors" 
              data-drag-handle 
              type="button"
              title="拖拽"
            >
              <GripHorizontal size={14} />
            </button>
            <div className="w-px h-3.5 bg-[#E6DFD8]" />
            <button 
              className="p-1.5 hover:bg-red-50 hover:text-red-500 transition-colors border-l border-[#E6DFD8]" 
              type="button" 
              onClick={() => props.deleteNode()}
              title="删除"
            >
              <Trash2 size={14} />
            </button>
          </div>
        </div>
      )}
`;

code = code.replace(
  /<div className="p-5 md:p-6">/,
  floatingMenu + '\n      <div className="p-5 md:p-6">'
);

// 4. Change grid-cols-1 md:grid-cols-3 to grid-cols-3 and add min-w
code = code.replace(
  /className="grid grid-cols-1 md:grid-cols-3 gap-4 min-h-\[260px\]"/,
  'className="grid grid-cols-3 gap-4 min-h-[260px] min-w-[700px]"'
);

// We should wrap the grid with an overflow-x-auto container to handle smaller screens if we force 3 columns
code = code.replace(
  /<div className="grid grid-cols-3 gap-4 min-h-\[260px\] min-w-\[700px\]">/,
  '<div className="overflow-x-auto pb-4 -mx-1 px-1 custom-scrollbar"><div className="grid grid-cols-3 gap-4 min-h-[260px] min-w-[760px]">'
);

code = code.replace(
  /<\/div>\n      <\/div>\n    <\/NodeViewWrapper>/,
  '</div>\n        </div>\n      </div>\n    </NodeViewWrapper>'
);

fs.writeFileSync('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/widgets/KanbanComponent.tsx', code);
console.log('Kanban fixed');
