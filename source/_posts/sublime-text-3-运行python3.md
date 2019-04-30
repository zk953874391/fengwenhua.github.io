---
title: sublime text 3 运行python3
mathjax: true
date: 2019-04-28 16:07:50
tags:
- sublime text 3 激活
categories:
- 软件配置
- sublime text 3
---

> sublime默认的是python2.7如果我想让他运行python3，怎么办呢?

1. 运行`which`命令找到`python3`的路径

```bash
which python3
```

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530637554.jpg)

<!--more-->
2. 自定义环境:`Tools`->`Build System`->`New Build System`,会弹出一个后缀为`sublime-build`的文件。

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530637688.jpg)

* ubuntu/deepin粘贴如下配置,如果发现pyqt5运行的时候啥也不显示，可将`"shell":"true"`删掉

```
{
    "cmd": ["/usr/bin/python3", "-u", "$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python",
    "shell":"true"
}
```

* windows粘贴下面的:
```
{
    "cmd":["E:\\Python\\Python36-32\\python.exe","-u","$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python",
    "encoding": "utf-8" ,
    "env": {"PYTHONIOENCODING": "utf8"},
    "shell":"true"
}
```

* mac粘贴下面的:

```
{
    "cmd": ["/usr/local/bin/python3", "-u", "$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python",
}
```

记住,其中的python3运行路径要和你系统中的路径一致,然后按`Ctlr+S`保存文件,文件名改为为`python3.sublime-build`，**保存的路径就是`Crtl+S`后默认的路径**,然后你在`Tools`->`Build System`,可以看到`python3`了,选择它再运行python,就会使用python3而不是python2.7了
