; Alt + '
!`::
    url := "https://www.kdocs.cn/l/cv9FaonW5wT8"
    targetTitle := "深圳拆建群 - 文档" ; 请根据实际网页标题调整此值

    ; 检查是否有匹配的窗口存在
    IfWinExist, ahk_exe chrome.exe
    {
        WinGet, id_list, List, ahk_exe chrome.exe
        Loop, %id_list%
        {
            this_id := id_list%A_Index%
            WinGetTitle, this_title, ahk_id %this_id%
            if InStr(this_title, targetTitle) ; 如果找到了匹配的标题
            {
                WinActivate, ahk_id %this_id% ; 激活该窗口
                return
            }
        }
    }

    ; 如果没有找到匹配的窗口，则打开新的标签页
    Run, %ComSpec% /c start chrome --new-tab "%url%",, Hide
return