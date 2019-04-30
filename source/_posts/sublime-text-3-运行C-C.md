---
title: sublime text 3 运行C-C++
mathjax: true
date: 2019-04-28 16:11:10
tags: 
- sublime text 3 运行C++
categories:
- 软件配置
- sublime text 3
---

* 点击`Tools`->`Build System`->`Build New System`

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190318114255.png)

<!--more-->
* 然后输入以下配置:

```
{
    "cmd": ["bash", "-c", "g++ '${file}' -std=c++11 -stdlib=libc++ -o '${file_path}/${file_base_name}'"],
    "file_regex": "^(..{FNXX==XXFN}*):([0-9]+):?([0-9]+)?:? (.*)$",
    "working_dir": "${file_path}",
    "selector": "source.c, source.c++",
    "variants":
    [
        {
        "name": "Run",
        "cmd": ["bash", "-c", "g++ '${file}' -std=c++11 -stdlib=libc++ -o '${file_path}/${file_base_name}' && open -a Terminal.app '${file_path}/${file_base_name}'"]
        }
    ]
}
```

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190318114320.png)

* 然后按`Command+S`保存,命名为`C/C++.sublime-build`,名字`C/C++`你随便起,但是**后缀名和保存路径不要改,默认就行**
> 该配置文件会保存在`/Users/用户名/Library/Application Support/Sublime Text 3/Packages/User`下

* 然后现在可以写c/c++的代码了,写完之后,点击`Tools`->`Build System`->`C:C++`
> 注意,因为我刚刚保存的时候文件名是`C/C++`,其中的`/`被自动替换成`:`了,所有`C:C++`也就是我刚刚保存的配置文件

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190318114333.png)

* 选择完编译器之后,按`Command+B`, 然后选择`C:C++ - Run`即可运行,下次直接按`Command+B`就可以运行了

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190328001827.png)
![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190318114346.png)
