zxl大屏程序

参考：https://www.cnblogs.com/Linux5500/p/11403313.html


一、程序打包
检查环境
1、pip install pyinstaller
2、pip install pycrypto
执行打包命令
3、python pyinstaller.py

二、提示 Microsoft Visual C++ 14.0 错误，根据以下安装
1、安装 Microsoft Visual C++ 14.0 选择 Windows 8.1 SDK 功能

2、复制 C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\include\stdint.h

3、粘贴 C:\Program Files (x86)\Windows Kits\10\Include\10.0.10240.0\ucrt

4、修改 C:\Program Files (x86)\Windows Kits\10\Include\10.0.10240.0\ucrt\inttypes.h

#include <stdint.h>
#include "stdint.h"
5、卸载 Micrsoft Visual C++ 14.0


三、安装PyCrypto以后出现的错误
https://www.jianshu.com/p/81594117bbc0