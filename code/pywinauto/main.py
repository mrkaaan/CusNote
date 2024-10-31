from pywinauto.application import Application

# https://blog.csdn.net/shawpan/article/details/78170117
# ----------------- 打开应用 -----------------
# 打开制定应用
# app = Application(backend="uia").start("notepad.exe")

# 打开任意应用程序
# app = Application(backend="uia").start(r"文件路径")
# app = Application(backend="uia").start(r"C:\Program Files (x86)\旺店通ERP\旺店通ERP.exe")

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

app = Application(backend="win32").connect(handle=132186)

# ----------------- 选择已打开应用 -----------------

# 方式一 app["类名/标题"]   推荐使用
# 类名选择窗口
# dlg = app["类名"]
# dlg = app["CoolWindow"]
dlg = app["Chrome Legacy Window"]

# 窗口标题选择窗口
# dlg = app["窗口标题"]

# 方式二 app.类名
# dlg = app.类名 # 这种方法也可以使用窗口标题选择窗口 但是不推荐 因为标题可能存在空格或中文

# 打印窗口中所有的控件
# dlg.print_control_identifiers()

# ----------------- 窗口操作 -----------------

# 最大化
# dlg.maximize()

# 最小化
# dlg.minimize()

# 还原
# dlg.restore()

# 关闭
# dlg.close()

# 查看窗口显示状态
status = dlg.get_show_state() # 1最大化 0正常
print(status)

# 获取当前窗口显示坐标
rect = dlg.rectangle() # (L, T, R, B) 从上到下，从左到右 依次距离屏幕左上角的距离
print(rect)

# ----------------- 窗口控件选择 -----------------

# 小的控件在大的控件里 比如“文件”在“菜单栏”里 可以使用ViewWizard 查看父类空间的标题或类名
# 也可以根据print_control_identifiers打印出来的控件层级选择 推荐

# 方式一
# 控件类名选择控件
# ctrl = dlg.控件类名

# 方式二
# 控件标题选择控件
# ctrl = dlg["控件标题/类名"]

# 选择子控件
# ctrl = dlg.控件类名.控件类名
# ctrl = dlg["控件标题/类名"]["控件标题/类名"]

# 如果子控件无法直接选择
# ctrl = dlg["控件标题/类名"].child_window(title="控件标题/类名", control_type="控件类名")

# ----------------- 控件分类 -----------------

# 状态栏 StatusBar
# 静态内容 Static
# 按钮 Button
# 复选框 CheckBoxControl
# 单选按钮 RadioButton
# 组合框 ComboBox
# 对话框 Dialog
# 编辑框 Edit
# 头部内容 Header
# 列表框 List
# 列表显示控件 ListView
# 弹出菜单 PopupMenu
# 选项卡控件 TabControl
# 工具栏 Toolbar
# 工具提示 ToolTips
# 树状视图 TreeView
# 菜单 Menu
# 菜单项 MenuItem
# 窗格 Pane
# 激活工具栏 ActionToolBar
# 标题栏 TitleBar

# ----------------- 获取控件类型 -----------------

# 获取控件类型 wrapper_object()

# 获取该控件支持的方法 dir(wrapper_object())

# 获取该控件的子元素 children()

# 获取该控件类名 class_name()

# 以字典形式返回控件的属性 get_properties()