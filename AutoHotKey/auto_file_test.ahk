
;---------------------快捷发送文件-------------------------

; 定义快捷短语和对应的文件路径
::pic1::  ; 当输入pic1并按空格时
SendPic("C:\Users\Kan\Desktop\test.png")  ; 替换为您的图片路径
return

; 自定义函数，用于复制文件路径到剪切板
FileCopy(filePath) {
    ClipWait, 1  ; 等待剪切板空闲
    ClipBoard := filePath  ; 将文件路径复制到剪切板

    ; 使用Windows命令行工具clip.exe将文件内容复制到剪切板
    ; RunWait, cmd /c clip.exe < %filePath%, , Hide
}

; 自定义函数，用于发送文件
SendPic(filePath) {
    ; 打开文件资源管理器到指定文件
    Run, explorer.exe, %filePath%
    Sleep, 500  ; 等待文件资源管理器打开
    ; 模拟鼠标点击选择文件
    MouseClick, left, 100, 100  ; 这里的坐标需要根据实际情况调整
    Sleep, 500
    ; 模拟按下Ctrl+C复制文件
    Send, ^c
    Sleep, 500
    ; 切换到聊天软件窗口
    WinActivate, 聊天软件窗口标题  ; 这里的标题需要根据实际情况调整
    Sleep, 500
    ; 模拟按下Ctrl+V粘贴文件
    Send, ^v
    Sleep, 500
    ; 模拟按下回车发送文件
    ; Send, {Enter}
}

; 自定义函数，用于复制文件内容到剪贴板
CopyFileContent(filePath) {
    FileRead, fileContent, %filePath%
    Clipboard := fileContent
    ClipWait
}

^+q::  ; 使用Ctrl+F5作为触发快捷键
  ClipSaved := ClipboardAll  ; 保存整个剪贴板内容
  Clipboard =  ; 清空剪贴板
  FileRead, Clipboard, *c <fullpath to saved file like D:\test.png>  ; 读取保存的文件到剪贴板
  MyErr := ErrorLevel  ; 获取错误级别
  if MyErr >= 1  ; 如果读取文件失败
  {
      MsgBox, Unable to read file!  ; 显示错误消息
  }
  else
  {
      ClipWait, 5  ; 等待剪贴板内容可用
      SendInput, ^v  ; 发送Ctrl+V进行粘贴
      Sleep, 2000  ; 延迟2秒，确保窗口有足够时间处理粘贴操作
  }
  Clipboard := ClipSaved  ; 恢复剪贴板内容
  ClipSaved =  ; 释放内存
Return