import bpy
import sys
import os
from pathlib import Path


def python_exec():
    try:
        # 2.92 and older
        path = bpy.app.binary_path_python
    except AttributeError:
        # 2.93 and later
        path = sys.executable
    return os.path.abspath(path)


# .blend FILEPATH
FILEPATH = Path(bpy.data.filepath).parent

# Add FILEPATH to sys.path
# so that custom modules can be found and imported
if FILEPATH not in sys.path:
    sys.path.append(str(FILEPATH))

# Change working directory to FILEPATH
os.chdir(str(FILEPATH))

# Install required modules with Blender python
os.system(python_exec() + " -m pip install -r requirements.txt")

# Execute blender_integration module
filename = FILEPATH / "blender_integration.py"
exec(compile(open(filename).read(), filename, 'exec'))
