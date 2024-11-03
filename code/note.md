pyautogui 简单教程
https://blog.csdn.net/Du_XiaoNan/article/details/136197235


pywinauto可以根据控件控制

支持控件的访问技术

确定程序该使用uia还是win32模式
https://www.cnblogs.com/baihuitestsoftware/articles/9317988.html
检测工具：
综合下载：https://github.com/blackrosezy/gui-inspect-tool

inspect： 检测UIA的
https://blog.csdn.net/qq_45451847/article/details/139271733
本地目录：C:\Program Files (x86)\Windows Kits\10\bin\10.0.20348.0\x64

SPYXX： 检测Win32的（有个望远镜 指定窗口

Viewwizard：https://github.com/deprecate1/ViewWizard/releases


#--------------------

python 镜像网站
https://mirrors.huaweicloud.com/python/3.12.5/

发现pywinauto无法获取字控件
转用pyautogui
发现现成pyautogui项目python-WinGUI：https://github.com/JoeyGambler/python-WinGUI

git clone https://github.com/JoeyGambler/python-WinGUI.git

需要环境Miniconda
Miniconda需要python312版本

conda env create -f environment.yml
conda activate gui

#--------------------
代理问题

https://cloud.tencent.com/developer/article/2405656
