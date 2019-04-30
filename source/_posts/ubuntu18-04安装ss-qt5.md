---
title: ubuntu18.04安装ss-qt5
date: 2018-11-15 14:59:55
mathjax: true
tags: ss-qt5
categories:
- Linux
- Ubuntu
---


> ~~今天ubuntu18.04正式版终于出来了,笔者等了好久了,于是马上官网下载下来安装一波.界面确实比16.04好看好多~~

* 安装18.04系统之后,当然少不了ss梯子了,然而,在安装`shadowsocks-qt5`的时候,安装16.04的安装方法如下:
```shell
sudo add-apt-repository ppa:hzwhuang/ss-qt5
sudo apt update
sudo apt install shadowsocks-qt5
```

* 然而在第二步update的时候出现了一个错误,如下
```
忽略: http://ppa.launchpad.net/hzwhuang/ss-qt5/ubuntu bionic InRelease
错误: http://ppa.launchpad.net/hzwhuang/ss-qt5/ubuntu bionic Release
    404  Not Found [IP:91.189.95.83 80]
```

<!-- more -->

* Are you kidding me?装不了ss?不存在的!吓得我马上上[shadowsocks-qt5](https://code.launchpad.net/~hzwhuang/+archive/ubuntu/ss-qt5)那里看了一下
* 原来是作者还没有测试18.04,这简单啊!将源中的`bionic`改成`artful`不就行了?
```
------>原来的如下:
http://ppa.launchpad.net/hzwhuang/ss-qt5/ubuntu bionic main
------>改成如下:
http://ppa.launchpad.net/hzwhuang/ss-qt5/ubuntu artful main
```
* 操作很简单(dan teng),点左下角九个点点,然后找到软件和更新->其他软件
> 这里一开始笔者是想找到`etc/apt/sources.list`来修改的,但是这个文件里看不到ss-qt5的源... ...

* 在这里修改ss-qt5的源,然后继续安装就行了.
* 接下来就是 enjoy your ubuntu
