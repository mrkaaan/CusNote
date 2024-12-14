@echo off
setlocal

:: 设置AutoHotkey的完整路径
set AHK_PATH=C:\software\AutoHotKey_cn\AutoHotKey\AutoHotkey.exe

:: 设置脚本变量
set SCRIPT_NAME=C:\note\customer_service_notes\AutoHotKey\AutoHotKey_New.ahk

:: 设置Python项目目录和文件名
set PYTHON_PROJECT_DIR=C:\note\python-WinGUI\src
set PYTHON_FILE_NAME=main.py

:: 运行AutoHotkey脚本
start "" "%AHK_PATH%" "%SCRIPT_NAME%"
echo AutoHotkey started successfully.

:: 进入Python项目目录
cd /d %PYTHON_PROJECT_DIR%
echo Directory changed successfully.

:: 激活Conda环境并运行Python文件
call conda activate gui && python %PYTHON_FILE_NAME%

:: 下面这种方法会导致关闭cmd后python程序仍然运行 需要手动到任务管理器结束python进程 慎用
:: 激活Conda环境并运行Python文件，忽略退出状态
::call conda activate gui
::start "" pythonw %PYTHON_FILE_NAME%
::echo Python script started.
:::: 暂停，等待用户按键
::echo Press any key to exit the batch script...
::pause >nul

endlocal