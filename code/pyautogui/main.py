# https://blog.csdn.net/Du_XiaoNan/article/details/136197235
# pyautogui

# https://www.cnblogs.com/johnnyzen/p/18026408

import pyautogui as pg
import time
import os

# -------------------------  屏幕 -------------------------
# 获取屏幕尺寸
# 元组类型的返回值
# screen_width, screen_height = pg.size()
# 获取屏幕宽高
# print("屏幕宽度:", screen_width)
# print("屏幕高度:", screen_height)

# -------------------------  暂停 -------------------------

#暂停操作，全局暂停，局部暂停
#全局暂停是指在程序中暂停所有操作（进行一行改代码，停一次，一般写在接口下面先执行），局部暂停是指在程序中暂停某个操作

#--------全局暂停--------
#默认是0.1  浮点型  单位是秒
# pg.PAUSE = 1.0

#--------局部暂停--------
#默认是0  浮点型  单位是秒
# time.sleep(2)

# -------------------------  保护 -------------------------

# 故障保护
# 当鼠标或键盘操作失败时，防止程序崩溃
# 在使用pyAutoGUI之前导入pyautogui.PAUSE(放在import之后 代码之前)
# pg.PAUSE = 1

# 程序执行中停止，快速移动到四个角
# pg.failsafe=false

# -------------------------  鼠标 -------------------------

# 获取鼠标位置的坐标值
# mouse_x, mouse_y = pg.position()
# print("鼠标位置的坐标值:", mouse_x, mouse_y)
#检测指定坐标是否在屏幕上 是否超出屏幕分辨率
# print("(100, 100)坐标是否在屏幕上:", pg.onScreen(100, 100)) # true
# print("(1930, 1090)坐标是否在屏幕上:", pg.onScreen(1930, 1090)) # false


#移动鼠标到指定位置
#duration是指所用时间，duration不写的话默认是0.25  浮点型  单位是秒
# pg.moveTo(100, 100, duration=1)
#移动鼠标到相对位置
# pg.move(100, -100, duration=1)


#鼠标拖拽操作
#默认左键，左键 left，右键 right,中键 middle
#绝对拖拽，指拖拽到那个位置
# pg.dragTo(x=100, y=-100, duration=0.5, button='left')
#相对拖拽，相对于当前位置拖拽
# pg.drag(xOffset=100, yOffset=100, duration=0.5, button='right')
# pg.drag(xOffset=-100, yOffset=0, duration=0.5, button='left')


#鼠标点击操作
#单击
#button:默认左键，左键 left，右键 right,中键 middle
#clicks:点击次数，默认是1次
#interval:每次点击间隔时间，默认是0
#duration:持续时间，默认是0
# pg.click(x=90, y=100,clicks=2,interval=0,duration=0, button='left')
# 双击
#button:默认左键，左键 left，右键 right,中键 middle
# pg.doubleClick(x=90, y=100, duration=0, button='left')


#单击分布操作
#按下鼠标键位
# pg.mouseDown(button='left')
#释放鼠标键位
# pg.mouseUp(button='left')


# -------------------------  键盘 -------------------------

# 键盘操作
#输入字符
#messge:想要输入的字符
#interval:每次输入间隔时间，默认是0
#不能直接输入中文，需要使用unicode编码
#输入时应先使输入框获取焦点，否则无法输入（可以先单击一下）
# pg.write("Hello, World!",interval=0.2)


#按键操作
#presses:按键的次数，默认是1次
#interval:每次按键间隔时间，默认是0
# pg.press('enter',presses=2,interval=0.2)


#热键操作
#interval:每次按键间隔时间，默认是0
# pg.hotkey('ctrl','a',interval=0.2)


# 所有按键的字符串标识如下
# print(pg.KEYBOARD_KEYS)

# -------------------------  消息框 -------------------------

#消息框
#title:标题
#text:文本
# button:按钮，默认是OK
#返回值：默认是OK
# arr1 = pg.alert(title='Hello, World!',text='没钱只能当牛马',button='ok')
# print(arr1)


#可以设置多个button
#返回值：返回用户点击的按钮
# arr2 = pg.confirm(title='Hello, World!',text='没钱只能当牛马',buttons=['ok','cancel'])
# print(arr2)


#自带文本输入框的消息框
#返回值：返回用户输入的内容
#文本输入框没字返回：None
# arr3=pg.prompt(title='Hello, World!',text='没钱只能当牛马',default='请您输入：')
# print("您输入的内容是："+arr3)


#自带密码的文本输入框的消息框
#返回值：返回用户输入的密码
#密码没字返回：None
# arr4=pg.password(title='Hello, World!',text='没钱只能当牛马',default='请您输入：',mask='*')
# print("您输入的密码是："+arr4)

# -------------------------  截图 -------------------------

# 设置截图的相对路径
# relative_path = "python_2024/all.png"
# 获取当前工作目录
# current_dir = os.getcwd()
# 构建绝对路径
# absolute_path = os.path.join(current_dir, relative_path)
# 检查目标文件夹是否存在，如果不存在则创建
# folder_path = os.path.dirname(absolute_path)
# if not os.path.exists(folder_path):
#     os.makedirs(folder_path)

# 保存截图
# pg.screenshot(absolute_path)
# print(f"Screenshot saved to {absolute_path}")

#屏幕截图
#imageformat:截图保存的格式，默认是png
#region:截图的范围，默认是整个屏幕
# 截取全屏 在1920 x 1080屏幕上，screenshot（）函数大约需要100毫秒-不快但不慢。
# 截取全屏，并以图片保存
# pg.screenshot("E:\\pythonDemo\\python_2024\\all.png")


#指定区域内截屏
#region:截图的范围，默认是整个屏幕 : [开始位置x,开始位置y,x扩展的分辨率,y扩展的分辨率]
# pg.screenshot("E:\\pythonDemo\\python_2024\\all2.png",region=[100,100,500,500])


#图片定位
#定位到的图片的坐标（从左到右，从上到下）
#image:图片路径
#confidence:定位精度，默认是0.8
#count:定位到的图片数量，默认是1
#返回图片中心点
# pg.locateCenterOnScreen("E:\\pythonDemo\\python_2024\\Google_tubiao.png",confidence=0.1)


