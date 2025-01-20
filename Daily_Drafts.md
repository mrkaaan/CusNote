# 暂存笔记 / 疑惑 / 需求

整理签收未收到
快捷判断苏宁当前用户是不是3504或873
打开已经打开的浏览器网页 快递表
如何文字视频一起发
通知错误提示
限制快捷键在指定软件生效 通过判断前置窗口


定位到表格最后一行

如何让浏览器可以复制发视频/快捷发视频
我需要使用浏览器登录一个客户网站 淘工厂的客服后台，在这个后台上接待进线的客户（Windows电脑端）
输入框上方有一个发送媒体文件的按钮，点击按钮后，在弹出的窗口中选择图片可以选择本地的图片选中并确认后可以进行发送。如何简化这个过程，这个过程的本质是什么

tk窗口的关闭后呼出

tk的两个窗口融合


视频压缩

让程序运行后在右下角有个小托盘
制作一个悬浮窗
检索electron的体积是否会影响性能 我的使用环境要求程序反应速度
测试浏览器插件和electron通信


杆子材质
防溅头材质
防溅头重量
桌面文件整理


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


广东省发货的呢，默认韵达快递。发货后省内一般是1-2天，省外的话3-4天左右的呢，具体看快递时效的亲爱的这边无法包快递保证的呢。运输路途上会给您多加催促的哦~~~

2号淘工厂
数显水龙头 深圳发
