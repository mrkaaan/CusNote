; 开机自启 autostart1则自启，0则删除自启
autostart:=1
autostartLnk:=A_StartupCommon . "\任意给个名字.lnk"
 
;----------auto start-------------
if(autostart) ;如果开启开机自启动
{
    IfExist, % autostartLnk
    {
        FileGetShortcut, %autostartLnk%, lnkTarget
        if(lnkTarget!=A_ScriptFullPath)
            FileCreateShortcut, %A_ScriptFullPath%, %autostartLnk%, %A_WorkingDir%
    }
    else
    {
        FileCreateShortcut, %A_ScriptFullPath%, %autostartLnk%, %A_WorkingDir%
    }
}
else
{
    IfExist, % autostartLnk
    {
        FileDelete, %autostartLnk%
    }
}

;------------------------解释----------------------------
; 是注释
; Ctrl 的符号是 ^ 
; Alt 的符号是 ! 
; Shift 的符号是 + 
; Win 的符号是#

;---------------------打开文件夹-------------------------
;不能用数字键盘的数字，要用主键盘的数字。

;打开文件夹project, Alt 3
!1::Run, C:\work

;打开文件夹project, Alt 3
!2::Run, C:\note

; 按下 Ctrl+Q 打开微信
^q::Run, C:\Program Files\Tencent\WeChat\WeChat.exe

; 按下 Alt+W 打开企业微信
!w::Run C:\Program Files (x86)\WXWork\WXWork.exe

; 按下 Alt+D 打开顶顶
!d::Run C:\Program Files (x86)\DingDing\DingtalkLauncher.exe

;---------------------打开网址-------------------------
;kimi
; Alt + k
!k::
    Run, https://kimi.moonshot.cn/
return

;鲁班
; Alt + NumPad0
!NumPad0::
    Run, https://order.lbdj.com/home/index
return

;潮州产品
; Alt + NumPad1
!NumPad1::
    Run, https://doc.weixin.qq.com/sheet/e3_AQkAHwZaABAQOapIY2CRaecuUfa3u?scode=ABsAQAckACEybVpl1lAUEAuAZzALA&tab=ymfwzv
return

; 潮州快递
; Alt + NumPad2
!NumPad2::
    Run, https://doc.weixin.qq.com/sheet/e3_AQkAHwZaABAzRNEplEHS96rWMcR8T?scode=ABsAQAckACEzUO8XukAUgAwQaNAOk&tab=BB08J2
return

; Alt + NumPad3
; 深圳产品
!NumPad3::
    Run, https://doc.weixin.qq.com/sheet/e3_AQkAHwZaABAi0oa07gjRrCTNTgq1E?scode=ABsAQAckACEQVh2eRJAUgAwQaNAOk&tab=BB08J2
return

; Alt + NumPad4
; 深圳快递
!NumPad6::
    Run, https://doc.weixin.qq.com/sheet/e3_AQkAHwZaABAKRXsV6t2SkOOj0FNI3?scode=ABsAQAckACEcASNeD6AUgAwQaNAOk&tab=j3wfob
return

;---------------------打开企业微信的对应群组-------------------------

; 定义一个函数，用于执行一系列操作
PerformAction(text) {
    Send, !{w}  ; 模拟按下 Alt + W
    Sleep, 500  ; 等待100毫秒

    Send, ^{f}  ; 模拟按下 Ctrl + F
    Sleep, 100  ; 等待100毫秒

    Send, ^{a}  ; 模拟按下 Ctel + A
    Sleep, 100  ; 等待100毫秒

    Send, {delete}  ; 模拟按下 Delete
    Sleep, 100  ; 等待100毫秒

    Send, {Shift down}  ; 按下Shift键
    Sleep, 100  ; 等待一段时间
    Send, {Shift up}  ; 释放Shift键
    Sleep, 100  ; 等待100毫秒

    Send, %text%  ; 输入传入的文本
    Sleep, 100  ; 等待100毫秒

    Send, {Shift down}  ; 按下Shift键
    Sleep, 100  ; 等待一段时间
    Send, {Shift up}  ; 释放Shift键
    Sleep, 100  ; 等待100毫秒

    Send, {Enter}  ; 发送一次向下按钮
    Sleep, 100  ; 等待100毫秒

    Send, {Enter}  ; 模拟按下回车键
}

; Alt + NumPad 4
!NumPad4::
    PerformAction("chaozhoucang-yunda")
return

; Alt + NumPad 5
!NumPad5::
    PerformAction("shenzhencang-yunda")
return

; Alt + NumPad 7
!NumPad7::
    PerformAction("chaozhoucangku")
return

; Alt + NumPad 8
!NumPad8::
    PerformAction("shenzhencangk")
return
