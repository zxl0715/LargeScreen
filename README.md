# LargeScreen

用python pythoninstaller cefpython 打造浏览器,查询机客户端,大屏(全屏)展示客户端

一、cefpython浏览器
介绍
用pythoninstall cefpython打包exe，制作自己的浏览器，

二、软件架构
PyInstaller: 3.5

Python: 3.7.3

Platform: Windows-10-10.0.17763-SP0

三、打包操作
运行pythoninstaller.py
可能会报错的地方
Microsoft visual c++ 14.0 is required问题

四、提示 Microsoft Visual C++ 14.0 错误，根据以下安装
1、安装 Microsoft Visual C++ 14.0 选择 Windows 8.1 SDK 功能

2、复制 C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\include\stdint.h

3、粘贴 C:\Program Files (x86)\Windows Kits\10\Include\10.0.10240.0\ucrt

4、修改 C:\Program Files (x86)\Windows Kits\10\Include\10.0.10240.0\ucrt\inttypes.h

#include <stdint.h>
#include "stdint.h"
5、卸载 Micrsoft Visual C++ 14.0

五、配置自己的窗口标题和默认打开页面
这里注意打包完成后，把目录中的config.ini复制到build中，否则启动报错

config.ini里面就是自定义口标题和默认打开页面的url
具体如下
[main]
#访问地址
url = https://www.baidu.com
#标题名称
title = 百度
#是否全屏
fullScreen=True
#屏幕宽度3840
width=1366
#屏幕高度1080
height=768
