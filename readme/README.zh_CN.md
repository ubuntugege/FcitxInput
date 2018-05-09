# FcitxInput
支持在Linux系统中使用[Fcitx](https://fcitx-im.org)输入简体中文/繁体中文/日文/韩文/越南文 到 Sublime Text

- 可创建启动支持Fcitx输入法的命令行程序
- 可创建启动支持Fcitx输入法的桌面快捷方式
- 已在Ubuntu/Fedora系统中测试过,也支持在其它Linux系统中使用

# README.md各语言版本
- en [English](../README.md)
- zh_CN [简体中文](README.zh_CN.md)
- zh_TW [繁体中文](README.zh_TW.md)

# 代码仓库镜像
- [GitHub](https://github.com/ubuntugege/FcitxInput)
- [OSC](https://gitee.com/ubuntugege/FcitxInput)
- [Coding](https://coding.net/u/ubuntugege/p/FcitxInput/git?public=true)

# 使用截图
#### 在Fedora中使用
![Work on OS X](https://raw.githubusercontent.com/ubuntugege/FcitxInput/shots/shots/sublime_fcitx_fedora.png)
#### 在Ubuntu中使用
![Work on Ubuntu](https://raw.githubusercontent.com/ubuntugege/FcitxInput/shots/shots/sublime_fcitx_ubuntu.png)

# 安装方法
- 通过Package Control安装
	- 首先要先安装 [Package Control](https://packagecontrol.io/installation)
	- 搜索 `FcitxInput` 并安装
- 手动下载安装(以下任选一)
	- 下载 [master.zip](https://github.com/ubuntugege/FcitxInput/archive/master.zip)安装包，解压到 `Packages`目录中，然后将 `FcitxInput-master` 命名为 `FcitxInput`
	- 使用git克隆到 `Packages`目录中
	```
	git clone https://github.com/ubuntugege/FcitxInput
	```

# 使用方法
- 在菜单中创建快捷方式
	- 依次展开菜单 `Tool` > `FcitxInput`
- 在命令面板中创建快捷方式
	- 用`Ctrl+Shift+P`打开命令面板, 输入`fci` 选择相应命令菜单
- 设置`st_exe`配置项(*只*在sublime text 2中需要)
	- `Preferences` > `Package Settings` > `FcitxInput` > `Settings - User`

# 提交问题
- [Github FcitxInput](https://github.com/zam1024t/FcitxInput/issues)

# 捐赠支持
- Paypal
	<br> [![用Paypal捐赠](https://raw.githubusercontent.com/ubuntugege/FcitxInput/shots/shots/donate_via_paypal.png)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=6J8DR2CCXPF9N)
- 支付宝
	<br> ![用支付宝捐赠](https://raw.githubusercontent.com/ubuntugege/FcitxInput/shots/shots/donate_via_alipay.png)
