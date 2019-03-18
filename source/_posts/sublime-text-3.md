---
title: sublime text 3
date: 2018-11-15 15:01:57
tags:
- sublime text 3
- st3
categories:
- 软件配置
---



> 本文来探究一下Ubuntu/Deepin/mac下sublime text 3的安装与配置

## 安装
### 下载与安装
> [点击打开官网](http://www.sublimetext.com/docs/3/linux_repositories.html)

* 终端下运行一下命令即可安装sublime text 3

```bash
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -

sudo apt install apt-transport-https

echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list

sudo apt update

sudo apt install sublime-text
```
<!-- more -->
### 激活

> 一般来说,直接输入下方秘钥即可激活成功,但是,sublime text 3会不定时的访问`license.sublimehq.com`,去检查秘钥的正确性,因此只能将该网址利用`hosts`屏蔽掉

> 注意:**先增加`Host 屏蔽`,然后输入秘钥才行**,以下是`hosts`文件的位置

```
* Windows : `c:/windows/system32/drivers/etc/hosts`
* Linux/Mac : `/etc/hosts`
```

* 在`hosts`文件最下面增加如下一行内容

```
127.0.0.1       license.sublimehq.com
```

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20181209171310.png)

* 保存退出`hosts`文件后,即可在sublime中输入秘钥,如下:

```
----- BEGIN LICENSE -----
sgbteam
Single User License
EA7E-1153259
8891CBB9 F1513E4F 1A3405C1 A865D53F
115F202E 7B91AB2D 0D2A40ED 352B269B
76E84F0B CD69BFC7 59F2DFEF E267328F
215652A3 E88F9D8F 4C38E3BA 5B2DAAE4
969624E7 DC9CD4D5 717FB40C 1B9738CF
20B3C4F1 E917B5B3 87C38D9C ACCE7DD8
5F7EF854 86B9743C FADC04AA FB0DA5C0
F913BE58 42FEA319 F954EFDD AE881E0B
------ END LICENSE ------
```

## ubuntu/deepin下无法输入中文

### 法一
> 以下方法是最快捷有效的方法,然而,可以输入中文了,但是,选择文件->右键->用`sublime text 3`打开,你会发现打不开文件了.但是先打开sublime,然后在里面选择文件又可以打开

```bash
git clone https://github.com/jfcherng/my_scripts

sudo apt install -y fcitx

sudo apt update

sudo apt install -y build-essential libgtk2.0-dev

cd my_scripts/sublime_text/sublime_text_fcitx

gcc -Os -shared -o libsublime-imfix.so sublime_imfix.c $(pkg-config --libs --cflags gtk+-2.0) -fPIC

sudo mv -f libsublime-imfix.so /opt/sublime_text

sudo cp -f subl "$(which subl)"

sudo cp -f sublime_text.desktop /usr/share/applications/

sudo cp -f sublime_text.desktop /opt/sublime_text
```

### 法二:

```shell
sudo apt update && sudo apt upgrade
git clone https://github.com/lyfeyaj/sublime-text-imfix.git
cd sublime-text-imfix && ./sublime-imfix
```

完成！**重新启动**后就可以在Sublime Text 3中使用搜狗输入法输入中文了
> 这里值得一提的是，博主用的是deepin，然后，一旦将st3固定在下面，然后，很快就又不能输入中文了，卸载重装即可

## 插件
### 安装package control
> 为了使用众多的插件来扩展 Sublime 的功能，你需要安装一个叫做 **Package Control **的插件管理器,一旦你安装好了以后，你就可以使用 `Package Control `来安装，**移除**或者**升级**所有的 ST3 插件了。

1.  按`Ctrl+~`打开控制台
2. 到 https://packagecontrol.io/installation#st3 获取安装代码,这里如下

    ```
    import urllib.request,os,hashlib; h = '6f4c264a24d933ce70df5dedcf1dcaee' + 'ebe013ee18cced0ef93d5f746d80ef60'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
    ```

3. 输入完了按`Enter`就行

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530636719.jpg)

4. 现在你可以通过快捷键 `Ctrl+Shift+P` 打开 `Package Control `来安装其他的插件了。输入 `install` 然后你就能看见屏幕上出现了 `Package Control: Install Package`，点击回车然后搜索你想要的插件。想装什么直接点击。注意看下面的`status bar`是显示进度的地方

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530636851.jpg)

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530636877.jpg)

### 安装`Anaconda` python插件
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

### SublimeREPL插件
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

### SublimeTmpl
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

### SideBarEnhancements
* 安装完后,可以在`View`->`Side Bar`->`Show Side Bar`打开

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20181209171421.png)

## 配置
### 隐藏mipmap和打开packages所在目录
1. `View`->`Hide minimap`:隐藏minimap

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530637060.jpg)

2. `Preferences`->`Browse Packages`:打开packages所在目录

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530637090.jpg)

### 设置运行python3
> sublime默认的是python2.7如果我想让他运行python3，怎么办呢?

1. 运行`which`命令找到`python3`的路径

    ```bash
    which python3
    ```
    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530637554.jpg)

2. 自定义环境:`Tools`->`Build System`->`New Build System`,会弹出一个后缀为`sublime-build`的文件。

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530637688.jpg)

    (1) ubuntu/deepin粘贴如下配置,如果发现pyqt5运行的时候啥也不显示，可将`"shell":"true"`删掉

    ```
    {
        "cmd": ["/usr/bin/python3", "-u", "$file"],
        "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
        "selector": "source.python",
        "shell":"true"
    }
    ```

    (2) windows粘贴下面的:
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

    (3) mac粘贴下面的:

    ```
    {
        "cmd": ["/usr/local/bin/python3", "-u", "$file"],
        "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
        "selector": "source.python",
    }
    ```

记住,其中的python3运行路径要和你系统中的路径一致,然后按`Ctlr+S`保存文件,文件名改为为`python3.sublime-build`，**保存的路径就是`Crtl+S`后默认的路径**,然后你在`Tools`->`Build System`,可以看到`python3`了,选择它再运行python,就会使用python3而不是python2.7了

### 一些常用的配置
打开`Preferences`->`Settings`,可以看到右边有个`settings-User`,我们修改这个文件就行

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530638088.jpg)

* 将一下配置粘贴进去就行
> 当然,这里本人是安装了`Boxy`主题的

```
{
    "font_size": 13,
    "ignored_packages":
    [
        "Vintage"
    ],
    "theme": "Boxy Monokai.sublime-theme",
    // 使用空格代替tab
    "translate_tabs_to_spaces": true,
    // 高亮未保存文件
    "highlight_modified_tabs": true,
    // 默认编码格式
    "default_encoding": "UTF-8",
    // 窗口失焦立即保存文件
    "save_on_focus_lost": true,
    // 保存时自动去除行末空白
    "trim_trailing_white_space_on_save": true,
    // 保存时自动增加文件末尾换行,这样 git 提交时不会生产额外的 diff
    "ensure_newline_at_eof_on_save": true,
    // 当前行高亮
    "highlight_line": true,
    // 设置行间距，看起来不那么"挤"
    "line_padding_bottom": 1,
    "line_padding_top": 1
}
```

* 另一种的配置

```
{
    "color_scheme": "Packages/Boxy Theme/schemes/Boxy Monokai.tmTheme",
    "default_encoding": "UTF-8",
    "ensure_newline_at_eof_on_save": true,
    "font_size": 12,
    "highlight_line": true,
    "highlight_modified_tabs": true,
    "ignored_packages":
    [
        "Vintage"
    ],
    "line_padding_bottom": 1,
    "line_padding_top": 1,
    "save_on_focus_lost": true,
    "theme": "Boxy Monokai.sublime-theme",
    "translate_tabs_to_spaces": true,
    "trim_trailing_white_space_on_save": true,
    "update_check": false
}
```


### Sublime常用快捷键
```
Ctrl+] 向右缩进
Ctrl+[ 向左缩进
Ctrl+Z 撤销。
Ctrl+Y 恢复撤销。
Ctrl+F 打开底部搜索框，查找关键字。
Ctrl+A 选中全文
Ctrl+B 运行python
Ctrl+Shift+P 调出命令窗
Ctrl+shift+R 格式化
Ctrl+shift+V 格式化粘贴 这个很有用，可以把网上的代码按照我的格式粘到我的文档里
Ctrl+//注释 这个比较厉害，如果是python,就是加#号的，想取消再弄一次就好了
```

### mac sublime text 3快捷键
```
[
    {
         "caption": "Tmpl: Create python", "command": "sublime_tmpl",
         "keys": ["ctrl+alt+n"], "args": {"type": "python"}
     },

    { "keys": ["ctrl+b"], "command": "build" },
    { "keys": ["ctrl+shift+b"], "command": "build", "args": {"select": true} },
    { "keys": ["ctrl+f"], "command": "show_panel", "args": {"panel": "find", "reverse": false} },
    { "keys": ["ctrl+s"], "command": "save" },
    { "keys": ["ctrl+x"], "command": "cut" },
    { "keys": ["ctrl+c"], "command": "copy" },
    { "keys": ["ctrl+v"], "command": "paste" },
    { "keys": ["ctrl+z"], "command": "undo" },
    { "keys": ["ctrl+shift+p"], "command": "show_overlay", "args": {"overlay": "command_palette"} },
    { "keys": ["ctrl+a"], "command": "select_all" },
    { "keys": ["home"], "command": "move_to", "args": {"to": "bol"} },
    { "keys": ["end"], "command": "move_to", "args": {"to": "eol"} },
    { "keys": ["shift+end"], "command": "move_to", "args": {"to": "eol", "extend": true} },
    { "keys": ["shift+home"], "command": "move_to", "args": {"to": "bol", "extend": true } }
]


```

### mac sublime text C/C++

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

### mac php

### 终端运行
```
{
    "cmd": ["php", "$file"],
    "file_regex": "php$",
    "selector": "source.php"
}

```

### 浏览器打开
> 前提mac要开启php

1. 安装`SidebarEnhancement`
2. 如下图

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20181205211354.png)

3. 输入以下代码

    ```
    {
        "/Library/WebServer/Documents/":{
            "url_testing":"http://localhost/",
            "url_production":""
        }
    }
    ```

4. **将你要编辑的php文件放在该目录下**:`/Library/WebServer/Documents/`编辑
5. 设置快捷键:

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20181205211635.png)

6. 输入以下代码,以后按`Ctrl+R`即可运行

    ```
    { "keys":["ctrl+r"],"command":"side_bar_open_in_browser","args":{"paths":[],"type":"testing","browser":"chrome"}},
    ```

### 安装boxy主题

* 复制附件两个文件到指定目录即可

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20181209201301.png)

### markdown
* Markdown Editing
* MarkdownPreview
> 在`Preferences` -> `Key Bindings`打开的文件的右侧栏的中括号中添加一行代码,然后用`Alt+M`就可以用浏览器打开了

```
{ "keys": ["alt+m"], "command": "markdown_preview", "args": {"target": "browser", "parser":"markdown"}  }
```

* LiveReload
> 安装成功后, 再次Ctrl+shift+p, 输入`LiveReload: Enable/disable plug-ins`, 回车, 选择 `Simple Reload with delay (400ms)`或者`Simple Reload`，两者的区别仅仅在于后者没有延迟。
> 只要你的sublime保存一次，网页那边就会自动刷新预览

* AdvanceNewFile
> 找到`"default_root": "project_folder",`，把`project_folder`改为`current`

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20181209202442.png)

## 5. 插件源被墙了
* 国内 https://packagecontrol.io 无法访问
* 解决办法链接: https://github.com/HBLong/channel_v3_daily
* 如下

```
1. 点击 Preferences > Package Settings > Package Control > Settings - User
2. 添加 "channels": ["https://raw.githubusercontent.com/HBLong/channel_v3_daily/master/channel_v3.json"],
```
