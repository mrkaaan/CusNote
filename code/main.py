import pyautogui as pg
import time

# 获取屏幕尺寸
# 元组类型的返回值
screen_width, screen_height = pg.size()
# 获取屏幕宽高
print("屏幕宽度:", screen_width)
print("屏幕高度:", screen_height)



#暂停操作，全局暂停，局部暂停
#全局暂停是指在程序中暂停所有操作（进行一行改代码，停一次，一般写在接口下面先执行），局部暂停是指在程序中暂停某个操作

#--------全局暂停--------
#默认是0.1  浮点型  单位是秒
# pg.PAUSE = 1.0

#--------局部暂停--------
#默认是0  浮点型  单位是秒
# time.sleep(2)



# 故障保护
# 当鼠标或键盘操作失败时，防止程序崩溃
# 在使用pyAutoGUI之前导入pyautogui.PAUSE(放在import之后 代码之前)
# pg.PAUSE = 1

# 程序执行中停止，快速移动到四个角
# pg.failsafe=false


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

