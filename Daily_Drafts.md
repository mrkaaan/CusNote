# 淘工厂相关

如何让浏览器可以复制发视频/快捷发视频
我需要使用浏览器登录一个客户网站 淘工厂的客服后台，在这个后台上接待进线的客户（Windows电脑端）
输入框上方有一个发送媒体文件的按钮，点击按钮后，在弹出的窗口中选择图片可以选择本地的图片选中并确认后可以进行发送。如何简化这个过程，这个过程的本质是什么


在开发浏览器插件的时候，如果我想要给某个在线聊天的网页添加一个提示功能，这个提示功能包括但不限于这些功能：新消息进线会有一个弹窗出现、弹窗不是浏览器窗口、弹窗脱离浏览器存在、弹窗窗口置顶、新消息显示在弹窗中（包含具体信息哪个浏览器、哪个页签、进线的用户、已经进线的计时）、每进线一人弹窗中便多一条消息、每回复一人弹窗中对应的消息并消失、按下设定好的快捷键即跳转到/置顶并聚焦最新进线的消息所在的浏览器的对应页签。这些功能如果使用浏览器本身的js和html会有很多功能实现不了，如果使用Native Messaging技术，是不是可以在有新消息进线和被回复时与本地工具沟通，用本地工具实现这些功能

在开发浏览器插件的时候，需要与本地的Electron程序通信，为了探究如何通信，我需要你实现这样一个功能，使用插件给当前页面添加一个输入框和一个按钮，按下按钮后，获取输入框中的内容，并将内容发送给Electron程序，Electron程序收到内容后，将内容显示在页面上

浏览器插件的环境已经配置完毕，electron的环境也配置完毕，现在需要实现插件与electron的通信，请问有什么好的实践方法吗？

下面有一篇文章可以参考一下，你认为用那种方式最好，先选用一种最简单的方式完成现在的这次demo，然后再考虑其他方案
参考实例：https://juejin.cn/post/6996918509338886180

输入框和按钮已经实现:
// 创建输入框并设置类名
const input = document.createElement('input');
input.className = 'electron-input';

// 创建按钮并设置类名
const button = document.createElement('button');
button.className = 'electron-button';
button.innerText = 'Send to Electron';

// 添加按钮点击事件监听器
button.addEventListener('click', () => {
    const data = input.value;
});

// 将输入框和按钮添加到#electronTestBox
electronTestBox.appendChild(input);
electronTestBox.appendChild(button);





完整进线回话结构
<div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_content"><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_info"><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_username" data-xreplay-desensitized-name="true" data-spm-anchor-id="0.0.0.i3.72ec7b96QhS47a">徐**7</div><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_tags"><span role="img" class="xixi-icon xixi-icon-mobile-o" style="color: var(--primary-color);"><svg width="1em" height="1em" fill="currentColor" focusable="false" aria-hidden="true"><use href="#xixi-icon-mobile-o"></use></svg></span><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_mask"></div></div></div><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_tips"><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_message">在呢亲</div><div><span class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-components-online-touch-timer_container"></span></div></div></div>


订单切换按钮的display
<div class="xixikf-biztarget-selector_components-biz-header_container" style="
    display: block;
"><div class="xixikf-biztarget-selector_components-biz-header_label">会员咨询的订单</div><div class="xixikf-biztarget-selector_components-biz-header_commands"><button data-component-id="xixi-design://button" tabindex="0" data-c-l-i="com.xixikf.imdesk.IMDeskApp>Plugin>com.xixikf.presale.applications.C2mbcBizTargetSelector/click-swap-to-biz-target-list-button" aria-label="点击修改咨询对象按钮" data-c-l-v="iBm_3LWW>lM2z6QXE/_" type="button" class="ant4-btn ant4-btn-default ant4-btn-icon-only xixi-button"><span role="img" class="xixi-icon xixi-icon-swap-o"><svg width="1em" height="1em" fill="currentColor" focusable="false" aria-hidden="true"><use href="#xixi-icon-swap-o"></use></svg></span></button></div></div>



系统消息
<div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_main"><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_avatar"><span class="ant4-badge xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_badge"><span data-component-id="xixi-design://avatar" class="ant4-avatar ant4-avatar-circle ant4-avatar-image xixi-avatar" style="width: 40px; height: 40px; line-height: 40px; font-size: 18px;"><img src="http://wwc.alicdn.com/avatar/getAvatar.do?type=sns&amp;userId=3296972685" data-spm-anchor-id="0.0.0.i76.294e7b96Xhbkgn"></span></span></div><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_content"><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_info"><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_username" data-xreplay-desensitized-name="true">t**0</div><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_tags"><span role="img" class="xixi-icon xixi-icon-mobile-o" style="color: var(--primary-color);"><svg width="1em" height="1em" fill="currentColor" focusable="false" aria-hidden="true"><use href="#xixi-icon-mobile-o"></use></svg></span><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_mask"></div></div></div><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_tips"><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_message" data-spm-anchor-id="0.0.0.i83.294e7b96Xhbkgn">[系统消息] 由于长时间未响应客服消息，系统将在60秒后自动结束会话，如果继续咨询请向客服提问。</div><div><span class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-components-online-touch-timer_container"></span></div></div></div></div>


新消息
<div data-id="new_25012192ENIW9yQ__fL2y3Ag775g"><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_wrap" id="im-desk-member-card-new_25012192ENIW9yQ__fL2y3Ag775g"><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_container xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_active"><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_flag xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card-online-touch-flag_container"><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card-online-touch-flag_hot-zone" tabindex="0" data-c-l-i="com.xixikf.imdesk.IMDeskApp>CustomSubjectProvider>com.xixikf.c2mbc.im.desk.extension.TaoFactoryOnlineTouchSubjectProvider/online-touch-flag" aria-label="在线会话角标" data-c-l-v="/_"></div><svg width="1em" height="1em" viewBox="0 0 16 16" version="1.1" xmlns="http://www.w3.org/2000/svg" class="session-empty-flag"><g stroke="none" stroke-width="1" fill="transparent" fill-rule="evenodd"><g transform="translate(-994.000000, -1813.000000)" stroke="#C5C9D4" stroke-width="2"><path d="M999.828427,1814 L1007,1814 C1009.20914,1814 1011,1815.79086 1011,1818 L1011,1825.17157 C1011,1826.27614 1010.10457,1827.17157 1009,1827.17157 C1008.46957,1827.17157 1007.96086,1826.96086 1007.58579,1826.58579 L998.414214,1817.41421 C997.633165,1816.63316 997.633165,1815.36684 998.414214,1814.58579 C998.789286,1814.21071 999.297994,1814 999.828427,1814 Z" transform="translate(1003.000000, 1822.000000) scale(-1, 1) translate(-1003.000000, -1822.000000) "></path></g></g></svg></div><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_main"><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_avatar"><span class="ant4-badge xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_badge"><span data-component-id="xixi-design://avatar" class="ant4-avatar ant4-avatar-circle ant4-avatar-image xixi-avatar" style="width: 40px; height: 40px; line-height: 40px; font-size: 18px;"><img src="http://wwc.alicdn.com/avatar/getAvatar.do?type=sns&amp;userId=33960483"></span></span></div><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_content" data-spm-anchor-id="0.0.0.i93.294e7b96Xhbkgn"><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_info"><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_username" data-xreplay-desensitized-name="true">z**1</div><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_tags"><span role="img" class="xixi-icon xixi-icon-mobile-o" style="color: var(--primary-color);"><svg width="1em" height="1em" fill="currentColor" focusable="false" aria-hidden="true"><use href="#xixi-icon-mobile-o"></use></svg></span><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_mask"></div></div></div><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_tips"><div class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-tao-factory-online-touch-explorer-member-card_message">终于等到您啦！欢迎光临本店，很高兴为您服务哒~</div><div><span class="xixikf-c-2-mbc-im-desk-extension_tao-factory-im-desk-components-online-touch-timer_container"></span></div></div></div></div></div></div></div>

# plan

整理签收未收到笔记

桌面文件整理

视频压缩

杆子材质

防溅头材质

防溅头重量

修改用户名
创建谷歌邮箱登录多个账号设置多个账号头像
https://blog.csdn.net/julius_lee/article/details/106802027

# imagine

## 无头绪

快捷判断苏宁当前用户是不是3504或873

打开已经打开的浏览器网页 快递表

如何文字视频一起发

通知错误提示

限制快捷键在指定软件生效 通过判断前置窗口

tk窗口的关闭后呼出

让程序运行后在右下角有个小托盘 - 打包程序

## 有头绪

tk的两个窗口融合


淘工厂通知悬浮窗：
更改标题
更改页签图标
更改通知左上角图标
更改通知文字通过params


程序运行通知

通知开始计时
通知结束时间

25 1 22 补发单号时 yemo3504 和 团结3504的 bug

多设置一些快捷键 16、18、16 18 等
龙头和取水嘴的视频一起发 的快捷键

选日期 点添加

淘工厂：
    主页
    账号图标
    任务栏图标
    自动启动八个并调整位置
    webtab

研究发送文件的本质流程

研究京东为前置窗口时无法使用工具的原因

鼠标侧键

ERP处理输入框内容异常：Expecting property name enclosed in double quotes: line 20 column 5 (char 792)


# 暂存笔记 / 疑惑 / 需求


您进入淘宝点击“我的淘宝”，选择“全部订单”，点进您的订单界面，您看下订单界面的实付款呢