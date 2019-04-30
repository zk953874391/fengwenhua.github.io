---
title: sublime text 3 激活
mathjax: true
date: 2019-04-28 15:55:58
tags: 
- st3激活
- sublime text 3 激活
categories:
- 软件配置
- sublime text 3
---

## 1. 原文链接
* https://www.52pojie.cn/thread-925256-1-1.html

## 2. 修改trigger
### 2.1. Windows
- 利用`010Editor`打开软件根目录下的`sublime_text.exe`
- 搜索16进制 `97 94 0D 00`
- 改为  `00 00 00 00`
- 保存
<!--more-->
> 已经修改好的文件: [sublime_text.exe](/files/sublime_text.exe)

### 2.2. Mac
- 拷出`/Applications/Sublime Text.app/Contents/MacOS/Sublime Text`
    
    > 其实就是 应用程序 文件夹下找到SublimeText应用，然后右键->显示包内容，然后打开/Contents/MacOS/ 然后找到 Sublime Text 这个文件 拷出来
    
- 利用`010Editor`打开它
- 搜索16进制 `97 94 0D 00`
- 改为  `00 00 00 00`
- 保存
- 打开终端，切换到当前目录
- 然后键入`chmod 755 Sublime\ Text`
- 替换掉`/Applications/Sublime Text.app/Contents/MacOS/Sublime Text`
- 完事儿

> 已经修改好的文件: [Sublime Text](/files/Sublime%20Text)

### 2.3. Linux
- 找个16进制编辑器(如`010Editor`)打开软件根目录下的`Sublime Text`
- 搜索16进制 `97 94 0D 00`
- 改为  `00 00 00 00`
- 保存
- 打开终端，切换到当前目录
- 然后键入`chmod 755 Sublime\ Text`
- 完事儿

## 3. 修改host
### 3.1. Windows
Windows的hosts文件在: 
```
系统盘:/windows/system32/drivers/etc/hosts
```

> Tips: Win下的权限获取可能有点复杂，不如先拷到桌面，编辑完替换回去。  
> 在最后一行插入

```
127.0.0.1 license.sublimehq.com
127.0.0.1 www.sublimetext.com
```

### 3.2. Mac
1. 打开Terminal(终端)
2. 输入 `sudo nano /Private/etc/hosts` 回车
3. 输入密码后回车
4. 在最后一行插入

```
127.0.0.1 license.sublimehq.com
127.0.0.1 www.sublimetext.com
```

5. 按下Control + X，输入Y确定修改，确认保存路径后敲击回车

### 3.3. Linux
同Mac

## 4. 激活
* 打开Sublime Text 3
* 选择`Help`-> `Enter License`
* 输入

```
----- BEGIN LICENSE -----
TwitterInc
200 User License
EA7E-890007
1D77F72E 390CDD93 4DCBA022 FAF60790
61AA12C0 A37081C5 D0316412 4584D136
94D7F7D4 95BC8C1C 527DA828 560BB037
D1EDDD8C AE7B379F 50C9D69D B35179EF
2FE898C4 8E4277A8 555CE714 E1FB0E43
D5D52613 C3D12E98 BC49967F 7652EED2
9D2D2E61 67610860 6D338B72 5CF95C69
E36B85CC 84991F19 7575D828 470A92AB
------ END LICENSE ------
```

* 选择`Use license`

## 5. 大功告成

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190428160029.png)

