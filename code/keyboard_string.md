# 所有按键的字符串标识如下
print(pyautogui.KEYBOARD_KEYS)
# 输出:
[
'\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 
'backspace', 'browserback', 'browserfavorites', 'browserforward', 'browserhome', 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear', 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail', 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab', 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen', 'command', 'option', 'optionleft', 'optionright'
]
+ 'Add' - 加号键（"+"）通常用于添加或增加操作。
+ 'Alt' - 通常与键盘上的 "Alt" 键相对应，它是一种常用的快捷键，可以用于访问特殊功能或菜单。
+ 'Altleft' - 这个单词通常与键盘上的 "Alt" 键左边的部分相对应，也是用于访问特殊功能或菜单。
+ 'Altright' - 这个单词通常与键盘上的 "Alt" 键右边的部分相对应，也是用于访问特殊功能或菜单。
+ 'Apps' - 右键菜单
+ 'Backspace' - 这个单词通常与键盘上的 "Backspace" 键相对应，用于删除前一个字符或命令。
+ 'Browserback' - 这个单词通常与浏览器相关的快捷键相对应，用于返回浏览器的上一个页面。
+ 'Browserfavorites' - 这个单词通常与浏览器相关的快捷键相对应，用于访问浏览器的收藏夹。
+ 'Browserforward' - 这个单词通常与浏览器相关的快捷键相对应，用于前进到浏览器的一个页面。
+ 'Browserhome' - 这个单词通常与浏览器相关的快捷键相对应，用于导航到浏览器的首页。
+ 'Browserrefresh' - 这个单词通常与浏览器相关的快捷键相对应，用于刷新当前页面。
+ 'Browsersearch' - 这个单词通常与浏览器相关的快捷键相对应，用于在浏览器中执行搜索操作。
+ 'Browserstop' - 这个单词通常与浏览器相关的快捷键相对应，用于停止加载当前页面。
+ 'Capslock' - 这个单词通常与键盘上的 "Capslock" 键相对应，用于锁定或解锁大写字母输入。
+ 'Ctrl' - 这个单词通常与键盘上的 "Ctrl" 键相对应，用于执行各种控制命令或组合键操作。
+ 'Ctrlleft' - 这个单词通常与键盘上的 "Ctrl" 键左边的部分相对应，也是用于执行各种控制命令或组合键操作。
+ 'Ctrlright' - 这个单词通常与键盘上的 "Ctrl" 键右边的部分相对应，也是用于执行各种控制命令或组合键操作。
+ 'Decimal' - 这个单词通常与键盘上的 "Decimal" 或 "." 键相对应，用于输入小数点或十进制数字。
+ 'fn' - "fn" 是一个特殊的键盘功能键，通常在笔记本电脑和一些特定的键盘布局中找到。它用于配合其他按键使用，以实现一些特定的功能，如调节亮度、音量等。
+ 'home' - "home" 对应的按键是键盘上的 "Home" 键，通常用于快速导航到页面的顶部或文本的开头。
+ 'insert' - "insert" 对应的按键是键盘上的 "Insert" 键，用于插入文本或数据。
+ 'left', 'right', 'up', 'down' - 这些方向键对应的按键分别是 "Left Arrow"、"Right Arrow"、"Up Arrow" 和 "Down Arrow"。它们通常用于控制光标的位置。
+ 'num0' 到 'num9' - 这些数字键对应的按键是从 "0" 到 "9"。它们用于输入数字和进行数学运算。
+ 'numlock', 'scrolllock', 'select', 'separator', 'tab' - 这些都是特殊的锁定键或其他功能键，通常用于控制光标移动、滚动页面、选择文本等操作。
+ 'space', 'return' - "Space" 键对应的按键是空格键，用于在文本中插入空格。"Return" 键对应的按键是回车键，用于换行或确认输入。
+ 'win', 'winleft', 'winright' - 这些是特定的功能键，通常用于操作系统中的窗口控制和菜单操作。"Win" 键对应的按键通常是 Windows 徽标键（通常是带有 Windows 标志的按键）。"Winleft" 和 "Winright" 是左右 Windows 功能键的称呼，但它们并不对应键盘上的标准按键
