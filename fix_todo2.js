const fs = require('fs');
let code = fs.readFileSync('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/widgets/TodoWidget.tsx', 'utf8');
code = code.replace(/import type { TodoTask, TodoList } from '\.\.\/\.\.\/contexts\/TodoContext';/, "import type { TodoTask } from '../../contexts/TodoContext';");
code = code.replace(/color\?: string;/, "");
code = code.replace(/color \n/, "\n");
fs.writeFileSync('/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/nova_repo/nova-block/src/components/widgets/TodoWidget.tsx', code);
