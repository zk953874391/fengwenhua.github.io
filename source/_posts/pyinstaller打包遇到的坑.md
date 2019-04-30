---
title: pyinstaller打包遇到的坑
date: 2018-11-27 12:46:05
mathjax: true
tags:
- pyinstaller
- pyqt打包
categories: Qt
---

# 打包
> 例子使用`pachonggui.py`

1. 正常执行一遍

    ```
    pyinstaller -Fw pachonggui.py
    ```
    <!--more-->
2. 给脚本加一行代码
    ```python3
    import PyQt5.sip
    ```
    然后再执行同样的命令
    ```
    pyinstaller -Fw pachonggui.py
    ```

3. 删掉`import PyQt5.sip`，可以继续写代码了。如果要打包，从`1`开始

## 出现`failed to execute script`的排查方法

### 法一:
命令执行完毕之后 `build\pachonggui\warnpachonggui.txt`,上面会**记载着错误**

### 法二:
```
# 使用完下面这条指令之后,打开exe,提示failed to execute script
pyinstaller -Fw pachonggui.py
# 然后执行下面这条执行,会在list下生成一个目录,进入该目录,用**命令行**执行该exe,就会看到错误了
pyinstaller -D pachonggui.py
```

```
pyinstaller打包使用pyqt5模块的时候，在win平台下，由于pyinstaller无法准确获取QT动态库文件路径，会报错导致无法打开运行程序，并提示错误信息pyinstaller failed to execute script pyi_rth_qt5plugins此时我们需要在打包的时候直接告诉pyinstaller到哪里去找，这个路径分隔符需要是unix形式：

pyinstaller --paths C:/****/Python/Python35-32/Lib/site-packages/PyQt5/Qt/bin -F -w ****.py
```

# pyqt5打包问题经过
> 这里用到的文件是`pachonggui.py`,里面使用了pyqt5 的库

安装好`pyinstaller`后,先使用下面的命令对脚本进行打包

```shell
pyinstaller.exe -Fw .\pachonggui.py
```


![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1533799324.jpg)

执行完毕,生成两个目录

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1533799377.jpg)

`exe`文件在`dist`目录下

双击运行出现`Failed to execute script pachonggui`错误

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1533799888.jpg)

先去`build`目录那里,找到`warn***.txt`文件,里面会记录一些错误

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1533799475.jpg)

这里可以看到,`pyqt5`的库没有找到

**分析**:正常来说,如果`pyinstaller`是`pip3`安装好的,那么`pyqt5`应该也在同一个目录下,应该不会出现找不到路径的情况.所以说,有两种情况,一个是`pyinstaller`错了,一个是`pyqt5`错了,这里我先指定`pyqt5`的路径让它试试

找到python3的安装路径,我的是如下

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1533800027.jpg)

然后使用`--path` 指定库目录,有一点需要注意:这里用的是`/`作为目录分隔符,而不是`\`

```shell
pyinstaller.exe --path E:/Python/Python36-32/Lib/site-packages/PyQt5/Qt/bin -Fw .\pachonggui.
py
```

重新打包之后,再次运行,报同样的错误,看`build`目录下的`warn***.txt`文件,还是同样的,没有找到`PyQt5`的库

因为本人安装了`python2.7`和`python3.6`,但是我只给python2.7配置了环境变量,所以说,命令行那里的`pyinstaller`是`python27`目录下的,而不是`python36-32`目录下的,所以说,接下来,我命令提示符那里指定使用`python36-32`下的`pyinstaller`试试

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1533800703.jpg)

执行打包命令之后,看到命令提示符,多了一些东西`sip not found`,不管它先,先记下来,然后继续运行一下`exe`

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1533800781.jpg)

没错,还是这个错误... ...

看一下`warn***.txt`

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1533800824.jpg)

发现pyqt5已经成功导入了,说明之前的错误原因真是因为调用了`python27`的`pyinstaller`,指定使用`python36-32`下的`pyinstaller`就没毛病了

这时候的`warn***.txt`是一大堆的看不懂的东西... ...怎么办?

没关系,还有办法,使用`-D`指令,将这个exe弄成一个目录,然后使用命令行去运行新目录下的exe,然后你应该会看到报错误了

```shell
E:\Python\Python36-32\Scripts\pyinstaller.exe -D .\pachonggui.py
```

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1533801080.jpg)

这时候`dist`目录下会多一个目录`pachonggui`

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1533801107.jpg)

然后,在这里,我需要使用`命令提示符`去运行这个`exe`

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1533801253.jpg)

结果如下:

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1533801281.jpg)

... ...`PyQt5.sip`是什么东东???我代码里面没有用到啊!!!~~~

在这种情况下,我决定,手动在代码里面加入它,然后再执行一次打包命令

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1533801753.jpg)

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1533801883.jpg)

不明白为什么提示`sip not found`还在,但是,这时候,exe已经可以运行,没有bug了
