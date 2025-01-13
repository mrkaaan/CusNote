# 暂存笔记 / 疑惑 / 需求

整理签收未收到
快捷判断苏宁当前用户是不是3504或873
打开已经打开的浏览器网页 快递表
如何文字视频一起发
通知错误提示
Everything搜索结果的位置 支架、粘贴、等
限制快捷键在指定软件生效 通过判断前置窗口

cmd中的操作如果输入了很多命令，按下上下就能切换记录，但是如果是新打开的cmd窗口是没有的，如何让新打开的cmd窗口也有这个功能。如何让cmd一进入后，直接按上键就能有记录，比如输入一条命令 python main.py，要的不是直接输入python main.py命令，而是有无办法把python main.py变成记录，按下上就能切换

假设我写了一个bat做了一系列操作，但是这些方式输入的命令貌似不算入历史，无法通过上下切换，所以能不能做一个这样的操作
等待上面的命令全都结束后，再执行下面的命令
发出ctrl+c信号，让程序停止
输入命令python main.py 但是要保证这个命令是记录，这样我就可以通过上下键切换

如何把cmd窗口放在小托盘
让程序运行后在右下角有个小托盘

杆子材质
防溅头材质

定位到表格最后一行

Everything插件 
everything toolbar

windows插件
powerToys run


我需要你给我一些灵感，我有计算机专业背景的知识，目前在做客服，工作背景是这样的
需要使用浏览器登录一个客户网站 淘工厂的客服后台 ，在这个后台上接待进线的客户
但是由于一个浏览器只能登录多个账号，一个客户要同时登录多个账号同时接待，所以要开启多个浏览器（至少8个）登录不同账号，调整不同的浏览器的位置层叠着保证全部浏览器窗口能同时前置显示

（都是Windows电脑端）
目前遇到的问题
1 这个后台如果有新客户进线只有在一个很小的文字提示 没有一个固定的悬浮窗上提示进线
2 因为提示文字很小 又有多个窗口 总是容易看漏




我有计算机专业背景的知识，目前在做客服，工作背景是这样的:需要使用浏览器登录一个客户网站 淘工厂的客服后台 ，在这个后台上接待进线的客户（都是Windows电脑端）
如果需要发送图片或者视频，输入框上方有一个发送媒体文件的按钮，点击按钮后，在弹出的窗口中选择图片可以选择本地的图片进行发送。但是，我的工作环境和我的个人喜好或者说我的需求是复制本地文件在输入框中粘贴发送，如果在聊天窗口粘贴的是图片可以，但是视频不行，如果是复制的视频，在输入框按下粘贴按键后是没反应的

给你看下错误的回答
回答1 使用自动化工具如Selenium、Puppeteer等编写一个脚本来处理视频的发送
错在哪： 我是实时操作，用什么自动化
回答2 如果淘工厂的客服系统提供了API接口，你可以尝试通过API上传视频
错在哪： 用api不论再怎么编程写工具不浪费时间吗
回答3 对于当前情况的一个快速解决方案是提供给客服人员一些技巧性的指导
错在哪：更是废话，我就是客服
我要的是具体解决问题的方法，代码已经给你， 给我解决问题

下面是输入框的HTML结构


-------------

窗口的关闭后呼出

如何让浏览器可以复制发视频

使用autohotkey的v1版本写一个快捷键
按下ctrl+空格是快捷键
后自动按下alt+空格，然后自动输入 “搜索” 自动按下回车 自动按下ctrl+v

灵感 使用autohotkey获取当前互动页签的url（不知道能不能判断多浏览器同时开启的情况）
https://blog.csdn.net/scy261983626/article/details/122817408


204
225
225-204=21

获取全部正在回话的
document.querySelectorAll("[class$='online-touch-explorer-member-card_wrap']")


数量
online-touch-explorer-virtual-touch-list_subject

online-touch-explorer-member-card_main

online-touch-explorer-member-card_info

online-touch-explorer-member-card_end-time

总数量
online-touch-explorer-closed-touch-list_collapsed
的
header
的
online-touch-explorer-closed-touch-list_number
旁边

document.querySelectorAll("[class$='online-touch-explorer-member-card_end-time']")
这样获取到了元素，如果不用爬虫，能不能计数同时只计数文本内容为 时时:分分 格式的数量

提示
online-touch-explorer-member-card_tips

online-touch-timer_container


使用浏览器拓展写一个插件
名称是 悉犀客服平台辅助工具
版本是1.0
作者是 mrkaan
图标 https://img.alicdn.com/imgextra/i1/O1CN01jTINIC1hfHKD8epcF_!!6000000004304-2-tps-80-80.png
描述是 提升使用悉犀客服平台的客服的使用体验，贴近千牛的使用习惯，正在开发中...
作用的网页是 https://c2mbc.service.xixikf.cn/im-desk  以及用作测试的 http://127.0.0.1:5500/code/test.html  （使用match做好*的通配）

功能：
1. 进入对应网站的提示 工具正在运行
2. 拦截ctrl+W关闭窗口的操作，弹出提示框
3. 判断某个元素是否存在（online-touch-timer_container,使用class$=），如果存在且里面有文本内容则使用Notification通知，要一直检查，每隔3s检查一次
title 为 淘工厂新消息，body为淘工厂有一条新消息尽快回复 (๑´ㅂ`๑) 
不需要icon和image，左上角图标使用默认不用设置，tag为‘淘工厂新消息提示’，已经显示过相同 tag 的通知也会再次提醒用户，通知会发出声音
4. 添加一个span 统计 document.querySelectorAll("[class$='online-touch-explorer-member-card_end-time']")
这样获取到了元素，能不能计数同时只计数文本内容为 时时:分分 格式的数量
放在
online-touch-explorer-closed-touch-list_collapsed （已存在元素）
的
header （已存在元素）
的
online-touch-explorer-closed-touch-list_number （已存在元素）
的右边
上面的都是使用document.querySelectorAll("[class$='']")获取到的，原本的class太长了

确保脚本在页面完全加载后执行
监听页面动态变化
使用 MutationObserver 监听页面动态变化
