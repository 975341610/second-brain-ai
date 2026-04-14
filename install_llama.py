import urllib.request
import os
import zipfile
import tempfile
import sys

# download the specific wheel for python 3.11 windows CPU
url = "https://github.com/abetlen/llama-cpp-python/releases/download/v0.3.7/llama_cpp_python-0.3.7-cp311-cp311-win_amd64.whl"

# Instead of doing that, let's write a script that the user can run locally.
