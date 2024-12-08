; 按下 Alt+Q 代替 Win+1 ~ Win+5

!q::  ; Alt + Q
{
    ; 循环发送 Win + 1 至 Win + 5
    Loop, 5
    {
        ; 发送 Win 加上当前循环索引作为数字键
        Send, #{%A_Index%}
        ; 等待一小段时间以确保每个组合键被正确处理 (可选)
        Sleep, 100
    }
    return
}