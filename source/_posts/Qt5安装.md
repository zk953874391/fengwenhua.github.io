---
title: Qt5安装
date: 2018-11-15 15:07:16
tags: Qt5安装
categories: Qt
---

# Windows

## 1. 安装Qt5
1. [点击进入Qt官网](http://download.qt.io/archive/qt/)下载Qt5,这里我下载的是最新版的`Qt5.11`,windows平台.


![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/_1527644391_16788_1537332597)
<!-- more -->
![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/_1527644458_5328_1537332616)
> tips:由于文件比较大,最好`右键->复制链接地址->打开迅雷`,用迅雷下载


2. 下载完成后,双击安装
3. 有三个地方要注意
    * 让你注册登录的时候,可以`Skip`跳过
    * 自行修改`安装路径`最好是`英文`的
    * 选择安装组件的时候,要`Select All`
    * 然后就是一路`Next`,最后`Install`了.
> tips:博主在安装过程中,会弹出一个`Installer Error`的警告,本人是直接点`Ignore`的,忽略此警告

3. 最后,点击`Finish`完成
4. 自此,Qt5的安装完毕

## 2. 配置Qt5的环境
### 2.1 安装windbg
> 默认情况下是没有`调试器`的，必须手动下载

[下载调试器windbg](https://developer.microsoft.com/zh-cn/windows/hardware/download-windbg),在安装过程中,**只勾选`Debugging Tools for Windows`,其他不选**

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/_1527645555_9264_1537332632)

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/_1527645589_21588_1537332640)

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/_1527645789_26375_1537332648)

### 2.2 验证
1. 打开 `Qt Creator`，`工具`->`选项`->`构建和运行`->`编译器`,进入编译器部分，可以看到 Qt 已经自动检测出来了，不需要手动配置

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/_1527652433_18573_1537332689)

2. 而`构建套件(Kit)`中,已经自动检测出来调试器了

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/_1527652386_4416_1537332701)

## 3. VS2017配置
### 3.1 安装插件Qt VIsual  Studio Tools
1. 打开VS2017->`工具`->`扩展和更新`

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/_1527652808_10732_1537332710)

2. `联机`->搜索框输入`Qt`->`Qt Visual Studio Tools`->`下载`,然后就会自动安装了,安装完成会提示重启VS2017

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/_1527652869_13419_1537332720)

3. 重启vs2017后,就会看到`Qt VS Tools`菜单项了

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/_1527653121_31687_1537332728)

### 3.2 插件配置
`Qt VS Tools`->`Qt Options`->`Add`->

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/_1527653495_12074_1537332742)

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/_1527653444_22807_1537332751)

## 4. Helloworld
> 配置好vs和qt的环境之后,接下来就是测试了,入门第一课:`Hello World`

打开`vs2017`->`文件`->`新建`->`项目`->`Visual C++`->`Qt`->`Qt GUI Application`->修改项目名称和位置->`确定`

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/_1527653727_2648_1537332766)

> tips: 要是发现自己没有`Visual C++`,右键`开始菜单`->`应用和功能`->`Visual Studio Professional 2017`->`修改`->找到`使用C++的桌面开发`->点击`修改`即可

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/_1527654327_13331_1537332777)


然后就是一路默认就行

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/_1527653743_10827_1537332797)

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/_1527653765_6383_1537332817)

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/_1527653782_30909_1537332828)

这时候,打开`main.cpp`,如下
```cpp
#include "QtHelloWorld.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QtHelloWorld w;
    w.show();
    return a.exec();
}
```

因为我们要打印一个`hello world`,所以说,简单改一下`main.cpp`代码,如下
```cpp
#include <QtWidgets/QApplication>
#include <QLabel>
int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    QLabel label("hello world");
    label.show();

    return a.exec();
}
```
结果如下:

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/_1527654005_20624_1537332840)


# Ubuntu
## 1. 安装pyqt5
```shell
sudo apt install pyqt5*
sudo apt install qt5-default
sudo apt install qttools5-dev-tools
```

## 2. 设置QtDesigner
* 打开pycharm后点击`File `- > `setting` - > `Tools`- > `External Tools,` 点击 `+` 号添加两个文件

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1535078798.jpg)

### 第一个文件---`QtDesigner`
```
/usr/bin/designer  # 填入Program
$FileDir$  # 填入Working directory
```

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1535078672.jpg)

### 第二个文件---`PyUIC`
```
/usr/bin/python3  # 填入Program
-m PyQt5.uic.pyuic  $FileName$ -o $FileNameWithoutExtension$.py  # 填入Arguments
$FileDir$  # 填入Working direction
```

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1535078710.jpg)

## 使用
>  在pycharm中的下拉菜单`Tools`中的`Qt5`就能看到刚刚定义的两个工具

