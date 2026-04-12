@echo off
echo ==========================================
echo [Nova] Windows CPU Installer for llama-cpp-python
echo ==========================================
echo This script will install llama-cpp-python using the official
echo pre-compiled wheel source to avoid C++ compilation errors.
echo.
python -m pip install https://github.com/abetlen/llama-cpp-python/releases/download/v0.3.19/llama_cpp_python-0.3.19-cp311-cp311-win_amd64.whl --force-reinstall --no-cache-dir
echo.
echo ==========================================
pause
