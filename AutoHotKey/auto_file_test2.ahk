
;---------------------快捷发送文件-------------------------
;------------------------解释----------------------------
; 是注释
; Ctrl 的符号是 ^ 
; Alt 的符号是 ! 
; Shift 的符号是 + 
; Win 的符号是#


#Persistent
#SingleInstance, force

; 定义快捷短语和对应的文件路径
::pic1::  ; 当输入pic1并按空格时
ClipSaved := ClipboardAll  ; 保存整个剪贴板内容
Clipboard =  ; 清空剪贴板
imageUtil.gdiplusStartup()
pBitmap := imageUtil.from_file("d:\test.png")  ; 替换为您的图片路径
if (pBitmap) {
    imageUtil.put_file(pBitmap, "Clipboard")  ; 将图片复制到剪贴板
}
imageUtil.gdiplusShutdown()
Clipboard := ClipSaved  ; 恢复剪贴板内容
return

::vid1::  ; 当输入vid1并按空格时
MsgBox, Video files cannot be copied to clipboard directly.
return

Class imageUtil {
    static gdiplusToken
    gdiplusStartup() {
        if (!gdiplusToken) {
            Gdip_Startup(gdiplusToken)
        }
    }
    gdiplusShutdown() {
        if (gdiplusToken) {
            Gdip_Shutdown(gdiplusToken)
            gdiplusToken := ""
        }
    }
    from_file(filePath) {
        if (!FileExist(filePath)) {
            return 0
        }
        hBitmap := 0
        DllCall("Gdiplus\GdipLoadImageFromFile", "str", filePath, "ptr*", hBitmap)
        if (hBitmap) {
            DllCall("Gdiplus\GdipCreateBitmapFromImage", "ptr", hBitmap, "ptr*", pBitmap)
            DllCall("Gdiplus\GdipDisposeImage", "ptr", hBitmap)
            return pBitmap
        }
        return 0
    }
    put_file(pBitmap, clipType) {
        if (clipType = "Clipboard") {
            DllCall("OpenClipboard", "ptr", 0)
            DllCall("EmptyClipboard")
            DllCall("Gdiplus\GdipGetHBITMAPFromBitmap", "ptr", pBitmap, "ptr*", hBitmap, "uint", 0)
            DllCall("SetClipboardData", "uint", 2, "ptr", hBitmap)
            DllCall("CloseClipboard")
            DllCall("Gdiplus\GdipDisposeImage", "ptr", pBitmap)
        }
    }
}

; 检测剪贴板变化
OnClipboardChange:
{
    if (A_EventInfo = 2) { ; 剪贴板中包含图片
        ClipboardIsPic := true
    } else {
        ClipboardIsPic := false
    }
    return
}