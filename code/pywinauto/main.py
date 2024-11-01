from pywinauto.application import Application

# 连接到旺店通ERP应用程序
app = Application(backend="win32").connect(handle=133920)

# 确保窗口是可见的并且被激活
dlg = app["旺店通ERP"]

# 打印控件标识符
# dlg.print_control_identifiers()

# order = dlg.child_window(title="订单管理", class_name="CoolWindow")
# order.print_control_identifiers()

# 获取所有直接子控件  
# for child in dlg.children():  
#     print(child.window_text())

# 获取所有子控件（包括嵌套子控件）  
# for descendant in dlg.descendants():  
#     print(descendant.window_text())


# print(dlg.wrapper_object()) # 获取控件类型
# print(dir(dlg.wrapper_object())) # 获取该控件支持的方法

# print(dlg.children) # 获取控件的子元素

# print(dlg.get_properties()) # 以字典形式返回控件的属性