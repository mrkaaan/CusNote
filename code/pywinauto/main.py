from pywinauto.application import Application

# https://blog.csdn.net/shawpan/article/details/78170117
# ----------------- 打开应用 -----------------
# 打开制定应用
app = Application(backend="uia").start("notepad.exe")

# 打开任意应用程序
# app = Application(backend="uia").start(r"文件路径")

# ----------------- 不确定哪种模式 -----------------

# 尝试使用Win32模式
# app_win32 = Application(backend="win32").connect(path="旺店通ERP的可执行文件路径")

# 尝试使用UIA模式
# app_uia = Application(backend="uia").connect(path="旺店通ERP的可执行文件路径")

# 根据连接和操作的结果，判断哪种模式更适合旺店通ERP

# ----------------- 连接已打开应用 -----------------
# 使用ViewWizard 查看进程号（PID）、句柄
# 进程号连接
# app = Application(backend="uia").connect(process=1234)

# 窗口句柄连接
# app = Application(backend="uia").connect(handle=1234)

# ----------------- 选择已打开应用 -----------------

# 方式一 app["类名/标题"]   推荐使用
# 类名选择窗口
dlg = app["类名"]

# 窗口标题选择窗口
# dlg = app["窗口标题"]

# 方式二 app.类名
# dlg = app.类名 # 这种方法也可以使用窗口标题选择窗口 但是不推荐 因为标题可能存在空格或中文

# 打印窗口中所有的控件
# dlg.print_control_identifiers()

# ----------------- 窗口操作 -----------------

# 最大化
dlg.maximize()

# 最小化
dlg.minimize()

# 还原
dlg.restore()

# 关闭
dlg.close()

# 查看窗口显示状态
status = dlg.get_show_state() # 1最大化 0正常

# 获取当前窗口显示坐标
rect = dlg.rectangle() # (L, T, R, B) 从上到下，从左到右 依次距离屏幕左上角的距离

# ----------------- 窗口控件选择 -----------------

# 小的控件在大的控件里 比如“文件”在“菜单栏”里 可以使用ViewWizard 查看父类空间的标题或类名
# 也可以根据print_control_identifiers打印出来的控件层级选择

