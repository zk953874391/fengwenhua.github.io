---
title: sublime text 3 Package Control被墙了
mathjax: true
date: 2019-04-28 16:09:29
tags: 
- Package Control被墙了
categories:
- 软件配置
- sublime text 3
---

* 国内 https://packagecontrol.io 无法访问
* 解决办法链接: https://github.com/HBLong/channel_v3_daily

### 1.1. 安装`Package Control`
1. 下载`Package Control.sublime-package`,放到`/Users/用户名/Library/Application Support/Sublime Text 3/Installed Packages`

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190328001858.png)
    <!--more-->
2. 重启`Sublime Text 3`

### 1.2. 本地使用
1. 去 https://github.com/HBLong/channel_v3_daily 下载`channel_v3.json`到`/User/用户名/`下,这里下载路径随便,我的是`/User/hua/`
2. 打开`Sublime Text 3`点击 `Preferences > Package Settings > Package Control > Settings - User`
3. 添加 `"channels": ["/User/用户名/channel_v3.json"],`

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190328001848.png)

### 1.3. 在线使用
1. 打开`Sublime Text 3`点击 `Preferences > Package Settings > Package Control > Settings - User`
2. 添加 `"channels": ["https://raw.githubusercontent.com/HBLong/channel_v3_daily/master/channel_v3.json"],`

接下来就可以愉快的用`Package Control`安装插件了
