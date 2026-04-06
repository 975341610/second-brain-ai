import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'second-brain-ai'))
import backend.api.routes
import inspect
print("File:", backend.api.routes.__file__)
lines, start = inspect.getsourcelines(backend.api.routes.note_to_response)
for i, line in enumerate(lines, start):
    print(f"{i}: {repr(line)}")
