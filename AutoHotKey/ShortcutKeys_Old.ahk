;------------------------解释----------------------------
; 是注释
; Ctrl 的符号是 ^ 
; Alt 的符号是 ! 
; Shift 的符号是 + 
; Win 的符号是#
; XButton1 鼠标侧键2
; XButton2 鼠标侧键1

;------------------------临时----------------------------

!Q::Enter
;---------------------不用的快捷键-------------------------
;+!Q::`
;+!E::~

;开启自动隐藏任务栏
;!3::Run, D:\001-software\taskbar\Turn_ON_auto-hide_taskbar.bat

;关闭自动隐藏任务栏
;!4::Run, D:\001-software\taskbar\Turn_OFF_auto-hide_taskbar.bat

;打开文件夹Alt Q代表QQ，不能用，用自带的快捷键Ctrl shift X
;!Q::Run, D:\QQ\Bin\QQScLauncher.exe

; ctrl+e = win+e

; ctrl+e = win+d

;---------------------打开文件夹-------------------------
;不能用数字键盘的数字，要用主键盘的数字。

;打开文件夹temp, Alt 2
!2::Run, D:\000-myfile\001-temp

;打开文件夹project, Alt 3
!3::Run, D:\project

;打开文件夹homework2, Alt 4
;!4::Run, D:\000-myfile\001-temp\homework2

;打开文件夹homework2, Alt m
;!m::Run, D:\002-game\mc

;打开文件夹Alt W代表wechat
!W::Run, D:\WeChat\WeChat.exe

;打开perfmon资源管理器
;+^1::Run, C:\Windows\System32\perfmon.exe

;打开文件夹 Alt E代表edge
;!E::Run, C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe

; Shift + Ctrl + F 使用默认浏览器打开翻译
; ^+F::Run https://fanyi.baidu.com/?aldtype=16047#auto/zh


; Win + J 使用默认浏览器打开百度
;#j::Run www.baidu.com


;---------------------搜索选中文字-------------------------

; 热键Ctrl + Shift + X 可以用百度搜索选中的文字
^+x::
{
 Send, ^c
 Sleep 50
 Run, https://www.baidu.com/s?wd=%clipboard%
 Return
}


;---------------------代替ALT+F4-------------------------
; Alt + 4 = Alt + F4
!4::!F4


; ---------------------代码快捷输入-------------------------
;system("pause");
::/sy::system("pause");


;<!-- -->
::/--::-- -->
; ---------------------快捷输入-------------------------

; 学号
::/xh::2010020118

; 身份证
::/sfz::130681200111031296

; 手机号1
::/sjh1::15778703972

; 手机号2
::/sjh2::19977753102

; QQ
::/qq::1960222170

; 邮箱
::/yx::1960222170@qq.com

; 邮箱
::/con::console.log("")

; 自定义项目编号
::/mys::
{
    Send, 1. {Space}{Enter}2. {Space}{Enter}3. {Space}{Enter}4. {Space}{Enter}5. {Space}{Enter}
    Return
}

;如何快捷的输入当前日期-2021年8月31日快捷输入当前日期的AutoHotkey热字串脚本
;一. # 开头表示指令, 通常是进行一些预处理或者设置, 比如
;#NoEnv ;不检查空变量是否为环境变量(建议所有新脚本使用).
;#NoTrayIcon ;不显示[托盘图标]
;#Hotstring EndChars `n `t ;自定义热字串终结符
#SingleInstance,force
#Persistent
;#NoTrayIcon
;~ 设置插入当前日期和时间的热字串为 rq 空格
;~ 用搜狗拼音输入法输入"rq"再按主键区数字2也可以方便快捷的输入当前日期，定义热字串使用两个冒号结尾, 以 return 束,如:
::/rq::
	Sleep,100
	ClipSaved := ClipboardAll ; 把剪贴板的所有内容保存到您选择的变量中
	Sleep,100
	NowTimeStr = %A_YYYY%-%A_MM%-%A_DD%
	Sleep,100
	Clipboard = %NowTimeStr%
	Sleep,200
	Send ^v
	Sleep,100
	Clipboard := ClipSaved ; 恢复剪贴板为原来的内容. 注意这里使用 Clipboard (不是 ClipboardAll).
	Sleep,100
	ClipSaved = ; 在原来的剪贴板含大量内容时释放内存.
return
