const fs = require('fs');
let code = fs.readFileSync('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/widgets/TodoWidget.tsx', 'utf8');

const target = `<button 
              onClick={() => setIsSettingOpen(!isSettingOpen)}
              className={\`p-2 border \${isDoodle ? 'border-2 border-black bg-white shadow-[2px_2px_0px_rgba(0,0,0,1)]' : 'border-border bg-background hover:bg-accent'} rounded-md transition-all \${isDoodle ? 'hover:translate-x-[1px] hover:translate-y-[1px] hover:shadow-none' : ''}\`}
            >
              <Settings size={20} className={s.text} />
            </button>`;

const replacement = `<button 
              data-drag-handle
              className={\`p-2 border \${isDoodle ? 'border-2 border-black bg-white shadow-[2px_2px_0px_rgba(0,0,0,1)]' : 'border-border bg-background hover:bg-accent'} rounded-md transition-all \${isDoodle ? 'hover:translate-x-[1px] hover:translate-y-[1px] hover:shadow-none' : ''} cursor-grab active:cursor-grabbing\`}
            >
              <GripHorizontal size={20} className={s.text} />
            </button>
            <button 
              onClick={() => props.deleteNode()}
              className={\`p-2 border \${isDoodle ? 'border-2 border-black bg-white shadow-[2px_2px_0px_rgba(0,0,0,1)] text-red-500' : 'border-border bg-background hover:bg-destructive hover:text-destructive-foreground'} rounded-md transition-all \${isDoodle ? 'hover:translate-x-[1px] hover:translate-y-[1px] hover:shadow-none' : ''}\`}
            >
              <Trash2 size={20} className={isDoodle ? "text-red-500" : ""} />
            </button>
            <button 
              onClick={() => setIsSettingOpen(!isSettingOpen)}
              className={\`p-2 border \${isDoodle ? 'border-2 border-black bg-white shadow-[2px_2px_0px_rgba(0,0,0,1)]' : 'border-border bg-background hover:bg-accent'} rounded-md transition-all \${isDoodle ? 'hover:translate-x-[1px] hover:translate-y-[1px] hover:shadow-none' : ''}\`}
            >
              <Settings size={20} className={s.text} />
            </button>`;

code = code.replace(target, replacement);

// check if NodeViewWrapper has data-drag-handle
code = code.replace(
  /<NodeViewWrapper \n      className={`([^`]+)`}\n      data-drag-handle\n    >/,
  '<NodeViewWrapper \n      className={`$1`}\n    >'
);

// check if rings are updated
code = code.replace(
  /<div className="absolute -top-12 -left-4 flex gap-2">\n            <div className="w-4 h-8 bg-gray-300 rounded-full border-2 border-black" \/>\n            <div className="w-4 h-8 bg-gray-300 rounded-full border-2 border-black" \/>\n            <div className="w-4 h-8 bg-gray-300 rounded-full border-2 border-black" \/>\n          <\/div>/,
  `<div className="absolute -left-6 top-8 flex flex-col gap-6">
            <div className="w-8 h-4 bg-gray-300 rounded-full border-2 border-black" />
            <div className="w-8 h-4 bg-gray-300 rounded-full border-2 border-black" />
            <div className="w-8 h-4 bg-gray-300 rounded-full border-2 border-black" />
          </div>`
);

fs.writeFileSync('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/widgets/TodoWidget.tsx', code);
console.log("Done");
