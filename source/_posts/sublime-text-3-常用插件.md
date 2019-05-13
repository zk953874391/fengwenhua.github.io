---
title: sublime text 3 常用插件
mathjax: true
date: 2019-04-28 16:13:17
tags:
- sublime text 3 常用插件
categories:
- 软件配置
- sublime text 3
---

### 0x01. 安装package control
> 为了使用众多的插件来扩展 Sublime 的功能，你需要安装一个叫做 **Package Control **的插件管理器,一旦你安装好了以后，你就可以使用 `Package Control `来安装，**移除**或者**升级**所有的 ST3 插件了。

1.  按`Ctrl+~`打开控制台
2. 到 https://packagecontrol.io/installation#st3 获取安装代码,这里如下

    ```
    import urllib.request,os,hashlib; h = '6f4c264a24d933ce70df5dedcf1dcaee' + 'ebe013ee18cced0ef93d5f746d80ef60'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
    ```

    <!--more-->

3. 输入完了按`Enter`就行

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530636719.jpg)

4. 现在你可以通过快捷键 `Ctrl+Shift+P` 打开 `Package Control `来安装其他的插件了。输入 `install` 然后你就能看见屏幕上出现了 `Package Control: Install Package`，点击回车然后搜索你想要的插件。想装什么直接点击。注意看下面的`status bar`是显示进度的地方

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530636851.jpg)

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530636877.jpg)
5. 现在是2019.3.18,不知道啥时候开始,sublime text3 的插件源就被墙了...,所以你们很可能装不了`Package Control`,因此,想办法番羽土蔷下载`Package Control`,或者百度一下下载吧! 离线安装好`Package Control`后,接下来如何操作请参考博主的另一篇博文

### 0x02. 安装`Anaconda` python插件
> [Anaconda](https://sublime.wbond.net/packages/Anaconda) 是一个终极 Python 插件。它为 ST3 增添了多项 IDE 类似的功能，其具体配置文件在 https://github.com/DamnWidget/anaconda 例如：

* `Autocompletion`:自动完成，该选项默认开启,按`TAB`或`Ctrl+Space`显示代码提示窗口
* `Goto Definitions`:能够在你的整个工程中查找并且显示任意一个变量，函数，或者类的定义。,键盘按下:`Ctrl+Alt+g`
* `Find Usage` 使用此命令，用户可以找到正在使用符号（变量，函数，方法，类或模块）的所有位置。键盘按下:`Ctrl+Alt+f`
* `Display Signatures`:能够显示一个函数或者类的说明性字符串(当然，是在定义了字符串的情况下)
![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530639346.jpg)

* `Show Documentation`： 可以查找并向用户显示任何函数，方法，类，模块或包的文档字符串。用户只需将光标放在想要获取文档字符串的符号上（或在括号之后，例如在写入之后`sys.exit()`),然后键盘按下`Ctrl+Alt+d`
* `Code linting`:使用支持 pep8 标准的 PyLint 或者 PyFlakes。因为我个人使用的是另外的 linting 工具，所以我会在 Anaconda 的配置文件 Anaconda.sublime-settings中将 linting 完全禁用。操作如下: `Sublime > Preferences > Package Settings > Anaconda > Settings – User： {"anaconda_linting": false}`
* 最后,配置一下Anaconda

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530639847.jpg)

```
{

"python_interpreter":"/usr/bin/python3",

"anaconda_linting": false,

//保存文件后自动pep8格式化

"auto_formatting": true,

// st3自动补全
"suppress_word_completions": true,
"suppress_explicit_completions": true,
//"complete_parameters": true
}

```

### 0x03. SublimeREPL插件
> `SublimeREPL`会新建一个交互式命令行界面,让你的py可以有输入

#### 配置python3环境
1. `Preferences`->`Browse Packages`,找到`SublimeREPL`的文件夹，再进入`config`文件夹，可以看到许多语言的配置文件，`Python`也在里面

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530640242.jpg)

2. 在`config`文件夹下新建`python3`文件夹,在里面新建`Default.sublime-commands`和`Menu.sublime-menu`两个文件(模仿Python文件夹),因为我们Python3目前只要**能打开shell运行，和运行这个脚本**，两个功能，因此就只要包含`Python3`和 `Python3 – Run current file`两项就好了
3. `Default.sublime-commands`配置如下：

    ```
    [
        {
            "caption": "SublimeREPL: Python3",
            "command": "run_existing_window_command", "args":
            {
                "id": "repl_python3",
                "file": "config/Python3/Main.sublime-menu"
            }
        },

        {
            "caption": "SublimeREPL: Python3 - RUN current file",
            "command": "run_existing_window_command", "args":
            {
                "id": "repl_python3_run",
                "file": "config/Python3/Main.sublime-menu"
            }
        }

    ]
    ```

4. `Menu.sublime-menu`配置如下：

    ```
    [
         {
            "id": "tools",
            "children":
            [{
                "caption": "SublimeREPL",
                "mnemonic": "R",
                "id": "SublimeREPL",
                "children":
                [
                    {"caption": "Python3",
                    "id": "Python3",

                     "children":[
                        {"command": "repl_open",
                         "caption": "Python3",
                         "id": "repl_python3",
                         "mnemonic": "P",
                         "args": {
                            "type": "subprocess",
                            "encoding": "utf8",
                            "cmd": ["python3", "-i", "-u"],
                            "cwd": "$file_path",
                            "syntax": "Packages/Python/Python.tmLanguage",
                            "external_id": "python3",
                            "extend_env": {"PYTHONIOENCODING": "utf-8"}
                            }
                        },
                        {"command": "repl_open",
                         "caption": "Python3 - RUN current file",
                         "id": "repl_python3_run",
                         "mnemonic": "R",
                         "args": {
                            "type": "subprocess",
                            "encoding": "utf8",
                            "cmd": ["python3", "-u", "$file_basename"],
                            "cwd": "$file_path",
                            "syntax": "Packages/Python/Python.tmLanguage",
                            "external_id": "python3",
                            "extend_env": {"PYTHONIOENCODING": "utf-8"}
                            }
                        }
                    ]}
                ]
            }]
        }
    ]
    ```

5. 保存文件后,就可以`Tools`->`SublimeREPL`->`Python3`运行命令了

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530640916.jpg)

6. 为了好看,采取和`Ctr+B`同样的上下布局

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530641055.jpg)

#### 设置key binding
每次这样到菜单栏里去找，太慢，能不能像`ctrl+B`一样直接运行呢？可以的，只要设置快捷键就好了，在`Preference`->`key Bindings-User`里

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530641287.jpg)

写入如下配置,即可`F4`运行`python2.7 repl`, `F5` 运行`python 3 repl`,**注意`id`还是要和`Menu.sublime-menu`文件里的`id`要一致，**

```
[
    {
        "keys":["f4"],

        "caption": "SublimeREPL: Python - RUN current file",

        "command": "run_existing_window_command", "args":

        {

            "id": "repl_python_run",

            "file": "config/Python/Main.sublime-menu"

        }

    },

    {
        "keys":["f5"],

        "caption": "SublimeREPL: Python3 - RUN current file",

        "command": "run_existing_window_command", "args":

        {

            "id": "repl_python3_run",

            "file": "config/Python3/Main.sublime-menu"

        }

    }
]

```

#### can't open file '$file_basename': [Errno 2] No such file or directory
这个只要再次用鼠标点击一下`test.py`就好了，就可以获取运行的文件了

### 0x04. SublimeTmpl
> 新建文件模板

1. 在`settings-user`写入以下信息

    ```
    {
        "disable_keymap_actions": false, // "all"; "html,css"
        "date_format" : "%Y-%m-%d %H:%M:%S",
        "attr": {
            "author": "江南小虫虫",
            "email": "fwh13612265462@gmail.com",
            "link": "http://www.fengwenhua.top"
        }
    }

    ```

2. `Ctlr+Alt+Shift+P`:默认创建python文件,这里进行修改.在`key bindings-user`中添加了以下信息，意思`ctrl+alt+n`就可以创建一个新的Python模板

    ```
         {
             "caption": "Tmpl: Create python", "command": "sublime_tmpl",
             "keys": ["ctrl+alt+n"], "args": {"type": "python"}
         },
    ```

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1532966184.jpg)


### 0x05. SideBarEnhancements
* 安装完后,可以在`View`->`Side Bar`->`Show Side Bar`打开

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20181209171421.png)
