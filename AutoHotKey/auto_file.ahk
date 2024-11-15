; 无用 + 中文问题无法解决 弃用

;---------------------快捷发送文件-------------------------
;------------------------解释----------------------------
; 是注释
; Ctrl 的符号是 ^ 
; Alt 的符号是 ! 
; Shift 的符号是 + 
; Win 的符号是#

#NoEnv  ; 排除环境变量
SendMode Input  ; 使用输入模式发送按键
SetWorkingDir %A_ScriptDir%  ; 设置工作目录为脚本目录

; 定义一个函数，将文件路径复制到剪贴板
SetFileToClipboard(filePath)
{
    RunWait, powershell -sta "$sc=New-Object System.Collections.Specialized.StringCollection; $sc.Add('" . filePath . "'); Add-Type -Assembly 'System.Windows.Forms'; [System.Windows.Forms.Clipboard]::SetFileDropList($sc)"
}

; 设置热字符串
::test1::  ; 当输入 "test1" 后跟一个空格时
    SetFileToClipboard("C:\test.png")  ; 替换为实际的文件路径
return

::test2::  ; 当输入 "test2" 后跟一个空格时
    SetFileToClipboard("C:\Users\Kan\Documents\Captura\2024-11-15-11-50-10.mp4")  ; 替换为实际的文件路径
return