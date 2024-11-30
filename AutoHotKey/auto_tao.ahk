; 初始化全局变量
currentWindow = 1

; 定义一个函数来切换窗口
SwitchWindows() {
    global currentWindow
    ; 根据当前窗口编号按下对应的 Win+数字键
    if (currentWindow = 1) {
        Send, ^1
    } else if (currentWindow = 2) {
        Send, ^2
    } else if (currentWindow = 3) {
        Send, ^3
    } else if (currentWindow = 4) {
        Send, ^4
    }
    ; 更新窗口编号，循环回到1
    currentWindow := (currentWindow % 4) + 1
}

; 定义热键 Alt+- 来调用 SwitchWindows 函数
!-::SwitchWindows()

; 检测鼠标的第二个侧键，这里假设是鼠标的第8个按钮（通常侧键是第8和第9个按钮）
; 你可能需要根据你的鼠标型号调整按钮编号
; 定义鼠标第二个侧键来调用 SwitchWindows 函数
Button8::SwitchWindows()