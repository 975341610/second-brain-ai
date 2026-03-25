@echo off
setlocal enabledelayedexpansion

:: 强制杀掉所有运行中的实例，释放文件
taskkill /F /IM SecondBrainAI.exe /T >nul 2>&1

echo ====================================================
echo   Performing Forced Clean Build - Bypassing Local Cache
echo ====================================================

echo Removing project build folder...
if exist "build" rd /s /q "build"

echo Removing frontend dist folder...
if exist "frontend\dist" rd /s /q "frontend\dist"

echo Updating frontend dependencies and building...
cd frontend
call npm install
call npm run build
cd ..

echo Running PyInstaller with --clean...
set "VERSION=unknown"
if exist "VERSION.txt" (
    for /f "usebackq delims=" %%v in ("VERSION.txt") do set "VERSION=%%v"
)

:: 获取 Git Hash
set "GIT_HASH=unknown"
for /f "tokens=*" %%i in ('git rev-parse --short HEAD 2^>nul') do set "GIT_HASH=%%i"

:: 生成 metadata.json
echo { "version": "!VERSION!", "git_commit": "!GIT_HASH!", "build_time": "%date% %time%" } > "metadata.json"

echo Current Version: !VERSION! (!GIT_HASH!)
call pyinstaller --clean second_brain_ai.spec

echo Cleaning up top-level standalone EXE in dist...
if exist "dist\SecondBrainAI.exe" del /f /q "dist\SecondBrainAI.exe"

echo ====================================================
echo   Clean Build Completed Successfully!
echo ====================================================
pause
