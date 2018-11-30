---
title: Qt遇到的一些坑
date: 2018-11-15 15:08:59
tags:
- IGL
- CURL_OPENSSL_3
- Openssl
categories:
- Qt
---


> 记得重新构建所有项目


### Could not determine which "make" command to run

#### 问题

```
21:48:20: Could not determine which "make" command to run. Check the "make" step in the build configuration.
Error while building/deploying project MarkdownPic (kit: Desktop Qt 5.11.1 GCC 64bit)
When executing step "qmake"
```

#### 解决
<!-- more -->
```
sudo apt install cmake g++ gcc gdb
```

然后打开`qtcreator`->`工具`->`选项`->`构建和运行`->`构建套件kit`->`自动检测的其中一项`->`编译器`，给C++也选择一个即可

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1535036707.jpg)

### `cannot find -IGL`
#### 解决

```
sudo apt install libgl1-mesa-dev
```

### `CURL_OPENSSL_3`
#### 问题

```
usr/lib/x86_64-linux-gnu/libcurl.so.4: version `CURL_OPENSSL_3' not found
```

#### 解决

```
# 先试一下下面的
sudo apt-get install libcurl4-openssl-dev

# 不行再用以下的
apt remove -y libcurl4
apt install -y libcurl4 curl
```

### 编译提示缺少`openssl`目录下一些问题件

#### 问题：

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1535036535.jpg)

#### 解决
```
sudo apt install libssl-dev
```
