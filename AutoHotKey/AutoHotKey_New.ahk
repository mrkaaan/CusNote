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

;打开文件夹project, Alt 1
!1::Run, C:\work

;打开文件夹project, Alt 2
!2::Run, C:\note

;打开文件夹project, Alt 3
!3::Run, C:\software

;打开文件夹project, Alt 4
!4::Run, C:\receptionData

; 按下 Ctrl+Q 打开微信
^q::Run, C:\Program Files\Tencent\WeChat\WeChat.exe

; 按下 Alt+W 打开企业微信
!q::Run C:\Program Files (x86)\WXWork\WXWork.exe

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

;潮州仓库产品问题
; Alt + NumPad1
!NumPad1::
    Run, https://doc.weixin.qq.com/sheet/e3_AQkAHwZaABAVylJxunsTwuCJbyyFq?scode=ABsAQAckACEroGgpYHAUEAuAZzALA&tab=BB08J2
return

; 潮州仓库快递问题
; Alt + NumPad2
!NumPad2::
    Run, https://doc.weixin.qq.com/sheet/e3_AQkAHwZaABAHJozL8lnScKkKV7Vfj?scode=ABsAQAckACED1n74eSAUEAuAZzALA&tab=BB08J2
return

; Alt + NumPad3
; 深圳仓库产品问题
!NumPad3::
    Run, https://doc.weixin.qq.com/sheet/e3_AQkAHwZaABAw51yfp5PRPSIDoC1C5?scode=ABsAQAckACEWu4yiMUAUEAuAZzALA&tab=BB08J2
return

; Alt + NumPad6
; 深圳仓库快递问题
!NumPad6::
    Run, https://doc.weixin.qq.com/sheet/e3_AQkAHwZaABAWORIPnieQwSk8hCYql?scode=ABsAQAckACEWJ0uKoTAUEAuAZzALA&tab=BB08J2
return


; Alt + NumPad9
; 多乐
!NumPad9::
    Run, https://www.kdocs.cn/l/coVsIfiNhaqN
return

; Alt + NumPadDiv /
; 银宾
!NumPadDiv::
    Run, https://www.kdocs.cn/l/cbyYlnoIbKtX
return

; Alt + NumPadMul *
; 罗刚
!NumPadMult::
    Run, https://www.kdocs.cn/l/ctLqaUf1xH6O
return

; Alt + M
; 支付宝返款登记表
!M::
    Run, https://kdocs.cn/l/cbYW6GJBCfjo
return

; Alt + L
; 查快递
!L::
    Run, https://www.kuaidi100.com
return

; Alt + ;
; 打开潮州拆建群
!;::
    Run, https://www.kdocs.cn/l/cpIw6wSo327f
return

; Alt + '
; 打开深圳拆建群
!'::
    Run, https://www.kdocs.cn/l/cv9FaonW5wT8
return

; Alt + /
; 打开傲迪厂家表
!/::
    Run, https://kdocs.cn/l/cg5wsAF4SaL6
return

;---------------------打开企业微信的对应群组-------------------------

; 定义一个函数，用于执行一系列操作
PerformAction(text) {
    Send, !{q}  ; 模拟按下 Alt + W
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

; 仓库 潮州
; Alt + NumPad 4
!NumPad4::
    PerformAction("zhoucangk")
return

; 快递 潮州 
; Alt + NumPad 5
!NumPad5::
    PerformAction("cang-y")
return

; 仓库 深圳
; Alt + NumPad 7
!NumPad7::
    PerformAction("zhencangk")
return

; 快递 深圳
; Alt + NumPad 8
!NumPad8::
    PerformAction("zhencangc")
return

; 提问群
; Alt + NumPad Add + 
!NumPadAdd::
    PerformAction("kefur")
return

; 发错货
; Alt + NumPad Sub - 
!NumPadSub::
    PerformAction("cuoh")
return

; 中通群
; Alt + NumPad del
!NumPadDel::
    PerformAction("zhongt")
return

; 先潮州 再深圳
; 问题表格 1产品2快递 3产品6快递
; 群 4仓库5快递 7仓库8快递

; Alt + [
; 潮洁开票
![::
    PerformAction("jied")
return

; Alt + ]
; 余猫开票
!]::
    PerformAction("maod")
return
