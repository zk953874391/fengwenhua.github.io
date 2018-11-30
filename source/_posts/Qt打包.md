---
title: Qt打包
date: 2018-11-15 15:05:24
tags:
- Qt打包
categories:
- Qt
---


## Windows打包
1. 首先我们是生成`Release`离线文件

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530156880.jpg)

2. 找到项目文件夹下生成的exe文件,如我的是`MarkdownPic.exe`,将该exe文件复制到一个新的文件夹,比如我将其复制到`C:\Users\13612\Dropbox\HMP`目录下
<!-- more -->
![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530157061.jpg)

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530157143.jpg)

3. 开始菜单搜索`qt`,然后找到`Qt 5.11.0 for Desktop`,打开运行,如下图

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530157277.jpg)

4. `cd`到`C:\Users\13612\Dropbox\HMP`目录
> ps:windows下,要先使用`C:`,切换到C盘,然后才能`cd`到C盘的子目录

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530157766.jpg)

5. 然后执行如下命令进行打包
```cmd
windeployqt MarkdownPic.exe
```

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530157915.jpg)

然后就可以看到如下效果,当然,如果你没有使用第三方的库,这个时候,你可以直接双击`MarkdownPic.exe`运行了,如果你使用了第三方的库,运行的时候会提示你缺少一些库文件,缺啥补啥就行

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530157948.jpg)

比如我使用了七牛云,就会出现如下的提示

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530158121.jpg)

将`dll`全部复制到`HMP`目录下,就可以**正常运行**了

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530158241.jpg)

6. 接下来就是程序发布阶段,我使用的是[Enigma Virtual Box](http://enigmaprotector.com/assets/files/enigmavb.exe),它可以将所有东西压缩到一个文件里面.操作如下
(1) `Browse`->`要打包程序`,这里是`MarkdownPic.exe`

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530158613.jpg)

(2) 将`HMP`目录下所有文件拖动到Enigma Virtual Box上,拖完后会弹框,选择`OK`即可,如下图

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530158777.jpg)

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530158795.jpg)

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530158818.jpg)

(3) 选择`Files Options`->勾选`Compress Files`

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530158877.jpg)

(4) 点击`Process`开始

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530158923.jpg)

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530158929.jpg)

(5) 打包完成,如下图,程序打包成了`MarkdownPic_boxed.exe`,可以拿这个exe去发布了,其他的文件都没有用了.

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530158967.jpg)

## Linux打包成Appimage
1. Release模式下生成离线文件

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/_1530165009.jpg)

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530165094.jpg)

2. 将其复制到一个空文件夹，这里是`fabuHMP`，然后`cd`到`fabuHMP`下

3. 使用`ldd`命令查看依赖库，发现有一个`libqiniu.so`不是系统自带的库，是第三方库，因此`ldd`命令在系统库那里找不到，需要添加环境变量，命令如下
![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/_1530160436.jpg)

```bash
# 用法如下：
export LD_LIBRARY_PATH=/Path/To/Lib:$LD_LIBRARY_PATH
# 我的是如下
export LD_LIBRARY_PATH=/home/hua/Dropbox/MarkdownPic/MarkdownPic-linux:$LD_LIBRARY_PATH
```

此时再执行`ldd MarkdownPic`，发现可以找到`libqiniu.so`库了

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530160735.jpg)

4. 下一步的操作是将所有的依赖库都复制到`fabuHMP`目录下，一个个复制粘贴太复杂，因此，需要用到shell脚本，如下
```bash
#!/bin/bash

exe="MarkdownPic" # 发布的程序名称
des="/home/hua/fabuHMP" # 你的发布程序存放路径
# 将 /home/hua/Dropbox/MarkdownPic/MarkdownPic-linux  替换成第三方库所在位置
export LD_LIBRARY_PATH=/home/hua/Dropbox/MarkdownPic/MarkdownPic-linux:$LD_LIBRARY_PATH
deplist=$(ldd $exe | awk  '{if (match($3,"/")){ printf("%s "),$3 } }')
cp $deplist $des
```

这时候，所以的依赖库都复制到`fabuHMP`目录下了

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530162548.jpg)


5. 添加`qmake`环境,编辑`.bashrc`文件
```
gedit ~/.bashrc`
```
在最后添加如下代码
```
#add QT ENV
export PATH=/home/hua/Qt5.11.1/5.11.1/gcc_64/bin:$PATH
export LD_LIBRARY_PATH=/home/hua/Dropbox/MarkdownPic/MarkdownPic-linux:$LD_LIBRARY_PATH
export QT_PLUGIN_PATH=/home/hua/Qt5.11.1/5.11.1/gcc_64/plugins:$QT_PLUGIN_PATH
```
重新打开一个终端，运行`qmake -v`,可以看到如下图则成功

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530164326.jpg)

6. 下载`linuxdeployqt`
[打开下载linuxdeployqt](https://github.com/probonopd/linuxdeployqt/releases)

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530163077.jpg)

重命名为 `linuxdeployqt`,并赋予可执行权限
```bash
sudo mv linuxdeployqt-continuous-x86_64.AppImage linuxdeployqt
chmod +x linuxdeployqt
```

移动到目录 `/usr/bin`
```
sudo mv linuxdeployqt /usr/bin
```

这时候终端执行`linuxdeployqt`可看到用法

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530163403.jpg)

7. 执行如下命令即可打包成一个`appiamge`，将该文件拷贝给其他人即可
```
linuxdeployqt MarkdownPic -appimage
```

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530165268.jpg)

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530165294.jpg)

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530164727.jpg)

## mac打包
```
pyinstaller --windowed --onefile --clean --noconfirm demo.py
pyinstaller --clean --noconfirm --windowed --onefile demo.spec
```

