# SublimeFcitx
支持在Linux系統中使用[Fcitx](https://fcitx-im.org)輸入簡體中文/繁體中文/日文/韓文/越南文 到 Sublime Text

- 可創建啟動支持Fcitx輸入法的命令行程序
- 可創建啟動支持Fcitx輸入法的桌面快捷方式
- 已在Ubuntu/Fedora系統中測試過,也支持在其它Linux系統中使用

# README.md各語言版本
- en [English](../README.md)
- zh_CN [簡體中文](README.zh_CN.md)
- zh_TW [繁體中文](README.zh_TW.md)

# 代碼倉庫鏡像
- [GitHub](https://github.com/ubuntugege/SublimeFcitx)
- [OSC](https://gitee.com/ubuntugege/SublimeFcitx)
- [Coding](https://coding.net/ubuntugege/SublimeFcitx)

# 使用截圖
#### 在Fedora中使用
![Work on OS X](https://raw.githubusercontent.com/ubuntugege/SublimeFcitx/shots/shots/sublime_fcitx_fedora.png)
#### 在Ubuntu中使用
![Work on Ubuntu](https://raw.githubusercontent.com/ubuntugege/SublimeFcitx/shots/shots/sublime_fcitx_ubuntu.png)

# 安裝方法
- 通過Package Control安裝
	- 首先要先安裝 [Package Control](https://packagecontrol.io/installation)
	- 搜索 `SublimeFcitx` 並安裝
- 手動下載安裝(以下任選一)
	- 下載 [master.zip](https://github.com/ubuntugege/SublimeFcitx/archive/master.zip)安裝包，解壓到 `Packages`目錄中，然後將 `SublimeFcitx-master` 命名為 `SublimeFcitx`
	- 使用git克隆到 `Packages`目錄中
	```
	git clone https://github.com/ubuntugege/SublimeFcitx
	```

# 使用方法
- 在菜單中創建快捷方式
	- 依次展開菜單 `Tool` > `SublimeFcitx`
- 在命令面板中創建快捷方式
	- 用`Ctrl+Shift+P`打開命令面板, 輸入`sfc` 選擇相應命令菜單
- 設置`st_exe`配置項(*只*在sublime text 2中需要)
	- `Preferences` > `Package Settings` > `SublimeFcitx` > `Settings - User`

# 提交問題
- [Github SublimeFcitx](https://github.com/zam1024t/SublimeFcitx/issues)

# 捐赠支持
- Paypal
	<br> [![用Paypal捐贈](https://raw.githubusercontent.com/ubuntugege/SublimeFcitx/shots/shots/donate_via_paypal.png)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=YL6ZR7Q4WGSQ4)
- 支付寶
	<br> ![用支付寶捐贈](https://raw.githubusercontent.com/ubuntugege/SublimeFcitx/shots/shots/donate_via_alipay.png)
