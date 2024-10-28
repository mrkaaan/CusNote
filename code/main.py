import pyautogui as pg
import time

# 获取屏幕尺寸
# 元组类型的返回值
screen_width, screen_height = pg.size()
# 获取屏幕宽高
print("屏幕宽度:", screen_width)
print("屏幕高度:", screen_height)
