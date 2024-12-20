# 自动化相关

pyautogui 根据屏幕坐标点击
pywinauto 根据控件控制 支持控件的访问技术 uia win32

## pywinauto

确定程序该使用uia还是win32模式
https://www.cnblogs.com/baihuitestsoftware/articles/9317988.html

检测工具:

综合 https://github.com/blackrosezy/gui-inspect-tool

inspect检测UIA的 https://blog.csdn.net/qq_45451847/article/details/139271733
> inspect安装后的本地目录：C:\Program Files (x86)\Windows Kits\10\bin\10.0.20348.0\x64

SPYXX： 检测Win32的（有个望远镜 指定窗口

Viewwizard：https://github.com/deprecate1/ViewWizard/releases


## pyautogui

发现pywinauto无法获取当前窗口（旺店通ERP、千牛）的句柄字控件，转用pyautogui

pyautogui 简单教程 https://blog.csdn.net/Du_XiaoNan/article/details/136197235

## python-WinGUI

发现现成pyautogui项目python-WinGUI：https://github.com/JoeyGambler/python-WinGUI

git clone https://github.com/JoeyGambler/python-WinGUI.git

需要环境Miniconda
Miniconda需要python312版本

部署指令：
···
cd python-WinGUI
pip install -r requirements.txt
python main.py
···

## conda

conda 环境管理工具

下载需要登陆后才能发送下载链接到邮箱，这里是下载链接：https://anaconda.cloud/api/iam/email/verified/f386a3e9-7d79-4a76-8463-ace9da27bfe9

conda 基础教程视频
https://www.bilibili.com/read/cv8956636/

conda代理
https://blog.csdn.net/sinat_27953939/article/details/134793098

另一个教程
https://sazerac-kk.github.io/p/%E6%95%99%E7%A8%8Bvscode-anaconda%E9%85%8D%E7%BD%AEpython%E7%8E%AF%E5%A2%83


### 安装后必做

CMD下初始化命令
conda config --set show_channel_urls yes

C盘用户目录下代理配置文件名（修改文件即配置代理）
.condarc

清除索引缓存（配置完毕后清理）
conda clean -i 


### conda 常用命令

查看已创建的环境
conda info -e 
conda env list

查看已安装的包
conda list

创建环境 缩写-n
conda create --name 环境明 包名=版本号

激活环境 只能同时激活一个环境
conda activate 环境名 

关闭环境
conda deactivate 

删除环境
conda remove --name 环境名 --all 
conda env remove --name 环境

安装包（在激活的环境下）
conda install --name 环境名 包名=版本号 包名2=版本号

删除包（在激活的环境下）
conda remove --name 环境名 --package 包名 

查找包
conda search 包名

查看指定环境下已安装的包
conda list -n gui 

查看当前环境下的包（conda）
conda list
查看当前环境下的包（pip）
pip list
> 报错缺包的话，分别查看conda和pip安装的包，对照environment.yml文件看哪些安装失败（如果是通过environment.yml安装的）

安装pip包 提示失败 Pip failed...
1. 重新安装pip包并忽略SSL验证
conda activate gui
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r environment.yml

2. 手动安装pip包 提前关梯子
pip install colorama==0.4.6 keyboard==0.13.5 loguru==0.7.2 mouseinfo==0.1.3 numpy==1.24.4 opencv-python==4.8.1.78 pillow==10.1.0 pyautogui==0.9.54 pygetwindow==0.0.9 pymsgbox==1.0.9 pyperclip==1.8.2 pypiwin32==223 pyrect==0.2.0 pyscreeze==0.1.30 pytweening==1.0.7 pywin32==306 win32-setctime==1.1.0


## conda 报错

ImportError: cannot import name '_pyautogui_win' from partially initialized module 'pyautogui' (most likely due to a circular import)

在 VScode 的状态栏中，确保激活的 Python 环境是 gui 环境
按 Ctrl+Shift+P（或 Cmd+Shift+P，在 macOS 上），搜索并选择 Python: Select Interpreter

# -------

# 资源 / 工具 / 解惑

## python 镜像网站

https://mirrors.huaweicloud.com/python/3.12.5/


## git 代理问题 

https://cloud.tencent.com/developer/article/2405656

## 输入法工具

https://www.appinn.com/inputtip-abgox/

https://inputtip.pages.dev/download/

## js呼出已存在的界面

https://blog.csdn.net/qq_16638125/article/details/115127573


## vscode前端插件

HTML Snippets 智能提示HTML标签，以及标签含义

JavaScript(ES6) code snippets 语法ES6智能提示，以及快速输入

Auto Rename Tag 自动完成另一侧标签的同步修改

Live Server 实时开发服务器插件

ESLint 用于JavaScript开发的静态代码检查工具

Auto Import 实现编写代码时自动导入所需的模块或组件

Path Intellisense 增强路径智能感知能力，书写相对或绝对路径时自动列出并补全项目内的文件和目录

JSON Tools 格式化json文件 使用时 shift+ctrl+p 搜索 json tool即可

## autohotkey 案例

https://blog.csdn.net/scy261983626/article/details/123102383
autohotkey自动点击

https://blog.csdn.net/scy261983626/article/details/122817408
autohotkey 指定网站的快捷键

## 谷歌浏览器插件

写可以在多个浏览器之前通信的谷歌浏览器插件

谷歌浏览器插件基础教程
https://blog.csdn.net/weixin_45491473/article/details/139421752

谷歌浏览器多开教程
https://zhuanlan.zhihu.com/p/6598046588

Node.js后端服务器：负责接收来自各个浏览器扩展的内容脚本的消息，并存储检测到的元素信息。同时，它也向浏览器扩展提供检测到的元素信息。
浏览器扩展的内容脚本：在每个浏览器标签页中运行，负责检测特定元素，并将其信息发送给Node.js后端服务器。
浏览器扩展的后台脚本：作为Node.js后端服务器与内容脚本之间的桥梁，负责接收内容脚本的消息并转发给后端服务器，以及从后端服务器获取检测到的元素信息并提供给悬浮窗。
浏览器扩展的悬浮窗：提供一个用户界面，显示所有检测到的元素信息，并允许用户点击这些信息以激活对应的浏览器标签页。


## x-mouse button control

可以修改鼠标按键的软件

目的是修改侧键为pageup和pagedown，便于在在线excel中快速下滑翻页

通常鼠标的两个侧键是 button4 和 button5
目前测试靠前侧键为 button5 靠后侧键为 button4

设置模拟按键：
{PGUP}
{PGDN}

间隔按下
{PGUP}{WAITMS:50}{PGUP}
{PGDN}{WAITMS:50}{PGDN}

长按
{HOLDMS:100}{PGUP}
{HOLDMS:100}{PGDN}

还是多次按下有用
{PGUP}{PGUP}{PGUP}
{PGDN}{PGDN}{PGDN}

如果表格最新记录就在最后一行，可以使用ctrl+down方向键快速翻到最后一行


## 千牛到处EMO格式表情分组

千牛分组表情注意事项：
表情含义和快捷符号限制长度限制为8
可中文长度同样限制为8
同名的快捷符号会覆盖
相同图片无法重复添加在同一组
切换分组前记得保存

导出后操作注意事项
- 导出为emo格式，后缀改为zip，解压
- 如果是导出全部则名称为 全部表情.emo
- 如果是导出某族则名称为 分组名称.emo
目录结构
```
├── 全部表情 / 分组名称
│   ├── 分组名称 (分组文件夹，有多少分组就有多少个)
│   │   ├── 表情.jpg （表情为md5命名，图片格式为jpg）
│   ├── ...
│   ├── config.json (配置文件)
```

- MyEmotion 为收藏夹默认分组
- 重新压缩为zip再改后缀emo即可导入，（需要用bandzip压缩，windows自带的压缩有问题会导入失败）
- 删除分组后不需要关闭表情编辑器，直接再次导入即可，不会导致有错乱（只有删除分组后分组内容为空但分组仍存在才需要重新打开表情编辑器再次删除才能删除）
- 导入后可以重复导入，会自动覆盖同名内容 不会导致有错乱

- 修改根目录文件夹名称不影响导入（压缩前修改和压缩后修改都可以）
- config.json 格式化后不影响导入
- 修改文件名及长度不会有错误(id/originalFile/fixedFile)
- id可以自定义 重复不报错 可任意修改
- 采用的应该是组合验证，删了id字段都没事
- fixedFile字段默认使用的是图片名称末尾加“fixedFile” 也可以自定义 也可以不添加 导入后会自动添加（根本不读这个字段）
- 图片名称用中文也可以
- png格式和jpg格式都可以
- config.json 里面数据在导入后会被自动编码处理
- type字段可以删除
- groupName也可以删除 因为图片默认在文件文件夹下 这个字段不会被读取
- 导入只会读取分组文件夹下的图片、config.json文件的shortCut、meaning、originalFile其他都可以删
- originalFile 字段唯一 如果需要多个图片则需要修改图片名称(如果不修改则后续相同的不会导入)

# -------



