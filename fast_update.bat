@echo off
setlocal enabledelayedexpansion
title Second Brain AI - Fast Update
cd /d "%~dp0"

set "ROOT=%~dp0"
set "OUT_DIR=C:\AI"
set "APP_DIR=%OUT_DIR%\SecondBrainAI"
set "VENV_PY=%ROOT%.venv\Scripts\python.exe"
set "VERSION=unknown"
if exist "%ROOT%VERSION.txt" (
    for /f "usebackq delims=" %%v in ("%ROOT%VERSION.txt") do set "VERSION=%%v"
)

:: 强制杀掉旧实例，防止文件被占用
taskkill /F /IM SecondBrainAI.exe /T >nul 2>&1

echo ==============================================
echo   Second Brain AI - 智能热更新 (!VERSION!)
echo ==============================================
echo.

if not exist "%VENV_PY%" (
    echo [!] 虚拟环境不存在，请先运行一次 build_windows.bat
    pause
    exit /b 1
)

echo [1/4] 正在清理旧的构建缓存...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

echo [2/4] 智能检测前端是否需要重新构建...

:: 默认不构建
set "BUILD_FRONTEND=0"

:: 用 PowerShell 检测：frontend（排除 node_modules/dist）中是否有比 frontend_dist 更新的文件
if not exist "%ROOT%frontend_dist" (
    echo [*] 未找到 frontend_dist，强制构建前端...
    set "BUILD_FRONTEND=1"
) else (
    for /f %%R in ('powershell -NoProfile -Command "$srcLatest = (Get-ChildItem -Recurse ''%ROOT%frontend'' -File | Where-Object { $_.FullName -notmatch ''\\node_modules\\'' -and $_.FullName -notmatch ''\\dist\\'' } | Sort-Object LastWriteTime -Descending | Select-Object -First 1).LastWriteTime; $distLatest = (Get-ChildItem -Recurse ''%ROOT%frontend_dist'' -File | Sort-Object LastWriteTime -Descending | Select-Object -First 1).LastWriteTime; if ($srcLatest -gt $distLatest) { echo 1 } else { echo 0 }"') do set "BUILD_FRONTEND=%%R"

    if "!BUILD_FRONTEND!"=="1" (
        echo [*] 检测到前端源码有更新，将重新构建...
    ) else (
        echo [*] 前端代码无变化，跳过构建。
    )
)

if "!BUILD_FRONTEND!"=="1" (
    echo [*] 正在执行前端构建 npm run build...
    cd /d "%ROOT%frontend"
    call npm run build
    if errorlevel 1 (
        echo [!] 前端构建失败，请检查 Node.js 环境。
        pause
        exit /b 1
    )
    cd /d "%ROOT%"
    if exist "frontend_dist" rmdir /s /q "frontend_dist"
    mkdir "frontend_dist"
    xcopy /e /i /y "frontend\dist" "frontend_dist" >nul
    echo [*] 前端构建完成，产物已同步到 frontend_dist。
)

echo [3/4] 正在重新打包后端 EXE...
"%VENV_PY%" -m PyInstaller second_brain_ai.spec --noconfirm --clean
if errorlevel 1 (
    echo [!] 打包失败，请检查报错。
    pause
    exit /b 1
)

:: 显式删除根目录下的冗余单体 EXE，以防混淆
if exist "dist\SecondBrainAI.exe" del /f /q "dist\SecondBrainAI.exe"

echo [4/4] 正在覆盖更新到 %APP_DIR% ...
taskkill /f /im SecondBrainAI.exe /t >nul 2>nul
timeout /t 1 >nul

:: 记录日志信息
echo [*] 正在同步构建产物...
echo     - 源路径:   %ROOT%dist\SecondBrainAI
echo     - 目标路径: %APP_DIR%
echo     - 版本号:   !VERSION!

:: 显式删除目标路径下可能残余的旧版单文件 exe (防止运行错误)
if exist "%APP_DIR%.exe" (
    echo [*] 正在清理旧版单文件 EXE...
    del /f /q "%APP_DIR%.exe"
)

:: 使用 robocopy 并检查严格错误码 (GEQ 8)
robocopy "dist\SecondBrainAI" "%APP_DIR%" /E /IS /IT /R:3 /W:5 >nul
if %ERRORLEVEL% GEQ 8 (
    echo.
    echo [!] ==================================================
    echo [!] 覆盖失败！(Robocopy ErrorLevel: %ERRORLEVEL%)
    echo [!] 请确保程序 %APP_DIR%\SecondBrainAI.exe 已完全关闭。
    echo [!] 请尝试以管理员权限运行此脚本。
    echo [!] ==================================================
    echo.
    pause
    exit /b 1
)

echo.
echo ==============================================
echo   ✨ 更新完成！
echo   程序位置: %APP_DIR%\SecondBrainAI.exe
echo   版本号:   !VERSION!
echo ==============================================
echo.
pause
exit /b 0
