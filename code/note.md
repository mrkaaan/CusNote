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

#--------------------

conda
基础教程
https://www.bilibili.com/read/cv8956636/
conda代理
https://blog.csdn.net/sinat_27953939/article/details/134793098
另一个教程
https://sazerac-kk.github.io/p/%E6%95%99%E7%A8%8Bvscode-anaconda%E9%85%8D%E7%BD%AEpython%E7%8E%AF%E5%A2%83

CMD下初始化命令
conda config --set show_channel_urls yes
C盘用户目录下代理配置文件名
.condarc

conda clean -i # 清除索引缓存，重新搜索包

conda info -e # 查看已创建的环境
conda env list # 查看已创建的环境 新版

conda list # 查看已安装的包

conda create --name 环境明 包名=版本号 # 创建环境 缩写-n
conda activate 环境名 # 激活环境 只能同时激活一个环境
conda deactivate # 关闭环境

conda remove --name 环境名 --all # 删除环境
conda env remove --name 环境名 # 删除环境 新版

conda install --name 环境名 包名=版本号 包名2=版本号 # 安装包
conda remove --name 环境名 --package 包名 # 删除包

conda search 包名 # 查找包

conda list -n gui # 进入环境前查看指定环境下的包
conda list # 查看当前环境下的包
pip list # 查看当前环境下的包
这种方法可以分别查看conda和pip安装的包，对照environment.yml文件看哪些安装失败

安装到pip的包 提示失败
Pip failed...
1 重新安装pip包并忽略SSL验证
conda activate gui
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r environment.yml

2 手动安装pip包 关代理
pip install colorama==0.4.6 keyboard==0.13.5 loguru==0.7.2 mouseinfo==0.1.3 numpy==1.24.4 opencv-python==4.8.1.78 pillow==10.1.0 pyautogui==0.9.54 pygetwindow==0.0.9 pymsgbox==1.0.9 pyperclip==1.8.2 pypiwin32==223 pyrect==0.2.0 pyscreeze==0.1.30 pytweening==1.0.7 pywin32==306 win32-setctime==1.1.0

# -------

conda 报错

## ImportError: cannot import name '_pyautogui_win' from partially initialized module 'pyautogui' (most likely due to a circular import)

在 VScode 的状态栏中，确保激活的 Python 环境是 gui 环境。
按 Ctrl+Shift+P（或 Cmd+Shift+P，在 macOS 上），搜索并选择 Python: Select Interpreter。