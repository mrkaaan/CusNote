@echo off
setlocal

:: 设置VSCode的完整路径，注意路径中的空格需要用双引号括起来
set "VSCODE_PATH=C:\Users\A\AppData\Local\Programs\Microsoft VS Code\Code.exe"

:: 设置AutoHotkey的完整路径
set AHK_PATH=C:\software\AutoHotKey_cn\AutoHotKey\AutoHotkey.exe

:: 设置脚本变量
set SCRIPT_NAME=C:\note\customer_service_notes\AutoHotKey\AutoHotKey_New.ahk

:: 设置Python项目目录和文件名
set PYTHON_PROJECT_DIR=C:\note\python-WinGUI\src
set PYTHON_FILE_NAME=main.py

:: 打开VSCode并打开指定的项目文件夹
start "" "%VSCODE_PATH%" "C:\note\customer_service_notes"

:: 打开两个VSCode窗口
start "" "%VSCODE_PATH%" "C:\note\python-WinGUI\"

:: 运行AutoHotkey脚本
start "" "%AHK_PATH%" "%SCRIPT_NAME%"
echo AutoHotkey started successfully.

:: 进入Python项目目录
cd /d %PYTHON_PROJECT_DIR%
echo Directory changed successfully.

:: 创建一个新的CMD窗口来激活Conda环境并运行Python文件
start cmd /k "call conda activate gui && python %PYTHON_FILE_NAME%"

endlocal