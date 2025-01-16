@echo off
setlocal

:: 设置VSCode的完整路径，注意路径中的空格需要用双引号括起来
set "VSCODE_PATH=C:\Users\A\AppData\Local\Programs\Microsoft VS Code\Code.exe"

:: 设置AutoHotkey的完整路径
set "AHK_PATH=C:\software\AutoHotKey_cn\AutoHotKey\AutoHotkey.exe"

:: 设置脚本变量
set "SCRIPT_NAME=C:\note\customer_service_notes\AutoHotKey\AutoHotKey_New.ahk"

:: 设置Python项目目录和文件名
set "PYTHON_PROJECT_DIR=C:\note\python-WinGUI\src"
set "PYTHON_FILE_NAME=main.py"

:: 使用/B保证按下ctrl+c后CMD窗口不会关闭
:: 打开VSCode并打开指定的项目文件夹
:: start /B "" "%VSCODE_PATH%" "C:\note\customer_service_notes"

:: 打开VSCode窗口，打开另一个项目文件夹
:: start /B "" "%VSCODE_PATH%" "C:\note\python-WinGUI\"

:: 运行AutoHotkey脚本
start /B "" "%AHK_PATH%" "%SCRIPT_NAME%"

:: 使用/k保证按下ctrl+c后CMD窗口不会关闭
:: 激活Conda环境并运行Python文件，保持CMD窗口打开
cmd /k "cd /d %PYTHON_PROJECT_DIR% && call conda activate gui && python %PYTHON_FILE_NAME% && ping localhost -n 2 >nul"

endlocal