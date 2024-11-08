;---------------------快捷启动-------------------------

SetTitleMatchMode 2  ; 设置窗口匹配模式，2表示部分匹配

; 定义一个函数来激活或打开窗口
ActivateOrOpen(title, exePath) {
    DetectHiddenWindows, On  ; 允许检测隐藏窗口
    If WinExist(title)  ; 检查窗口是否存在
    {
        WinShow, ahk_exe %exePath%  ; 显示窗口
        WinActivate  ; 激活窗口
    }
    Else  ; 如果窗口不存在
    {
        Run, %exePath%  ; 运行ERP软件
    }
    DetectHiddenWindows, Off  ; 关闭检测隐藏窗口
}

; 绑定快捷键，例如使用 Ctrl+Alt+E 来激活或打开ERP软件
^!e::ActivateOrOpen("旺店通ERP", "C:\Program Files (x86)\旺店通ERP\旺店通ERP.exe")