const fs = require('fs');

let code = fs.readFileSync('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/widgets/TodoWidget.tsx', 'utf8');

code = code.replace(/<button \n              className="p-1.5 hover:bg-red-50 hover:text-red-500 transition-colors border-l border-\[#E6DFD8\]" \n              type="button" \n              onClick={\(\) => props\.deleteNode\(\)}\n              title="删除"\n            >/g, 
  '<button \n              className="p-1.5 hover:bg-red-50 hover:text-red-500 transition-colors border-l border-[#E6DFD8]" \n              type="button" \n              onClick={() => deleteNode()}\n              title="删除"\n            >');

fs.writeFileSync('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/widgets/TodoWidget.tsx', code);
