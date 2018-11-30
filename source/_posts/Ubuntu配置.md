---
title: Ubuntu配置
date: 2018-11-15 14:57:15
tags: ubuntu配置
categories:
- Linux
- Ubuntu
---

# 必备基础
### 更新
```shell
sudo apt update
sudo apt upgrade
sudo apt dist-upgrade
```


### 软件安装
### 软件包里有的软件(一般都是这个)
```shell
sudo apt install 软件名
```
### `.deb`结尾的文件
```shell
sudo dpkg -i 软件名
```

<!-- more -->

### 解除依赖
```shell
sudo apt -f install
```

### Ubuntu中软件包管理
 1.下载的软件存放位置
```
/var/cache/apt/archives
```
 2.安装后软件默认位置
```
/usr/share
```
3.可执行文件位置
```
/usr/bin
```
4.配置文件位置
```
/etc
```
5.lib文件位置
```
/usr/lib
```

---

# 以下为常用的各种软件

### vm-tool(虚拟机才会使用,用于全屏,复制)
```shell
sudo apt install open-vm-tools-desktop fuse
```

### 删除基本不用的自带软件
```shell
sudo apt purge libreoffice-common unity-webapps-common thunderbird totem rhythmbox  simple-scan gnome-mahjongg aisleriot gnome-mines cheese transmission-common gnome-orca webbrowser-app gnome-sudoku  onboard deja-dup
```

### shadowsocks-qt5(ubuntu18.04失效)
```shell
sudo add-apt-repository ppa:hzwhuang/ss-qt5
sudo apt update
sudo apt install shadowsocks-qt5
```
### proxychains4
> 借助它，ss才能终端翻墙

```shell
git clone https://github.com/rofl0r/proxychains-ng.git
cd proxychains-ng
./configure --prefix=/usr --sysconfdir=/etc
make
sudo make install
sudo make install-config
```
然后还要编辑一下proxychains的配置文件
```
sudo gedit /etc/proxychains.conf
# 如果你之前安装过proxychains,那么这时候的配置文件应该是proxychains4.conf,但是在进行以下修改的时候，两个配置文件都要修改
```

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530169409.jpg)

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530169442.jpg)

### 安装必要软件
```shell
sudo apt install vim ctags  git  gcc gdb rar diffuse shutter curl
```


* `vim`:强大的编辑器
* `git`:代码管理
* `gcc`,`gdb`,`ctags`:编译C语言用到
* `rar`:解压.rar压缩文件
* `diffuse`:文件比对
* `shutter`:一款截图软件,快捷键：shutter --select)
* `curl`:一般我用来测试proxychains4
### 安装Oracle Java
```shell
sudo add-apt-repository ppa:webupd8team/java
sudo apt update
sudo apt install oracle-java8-installer
```

### 安装WPS
* 官网下载WPS(.deb): http://community.wps.cn/download/
* `dpkg -i 包名`,进行安装
* `sudo apt -f install`,解除依赖


### 安装网易云
* 官网下载网易云：http://music.163.com/#/download
* `dpkg -i 包名`
* `sudo apt -f install`
* 运行：`sudo netease-cloud-music`

### 安装搜狗输入法
* 官网下载搜狗输入法： http://pinyin.sogou.com/linux/?r=pinyin
* `dpkg -i 包名`
* `sudo apt -f install`
* 重启即可
##### 若出现无法输入中文
普通用户,不用提权
```shell
cd ~/.config
find . -name sogou*
find . -name Sogou*
```
将那三个文件干掉即可
##### 若想输入英文标点
**Ctrl+.**

### Flatabulous主题
```shell
sudo add-apt-repository ppa:noobslab/themes
sudo add-apt-repository ppa:noobslab/icons
sudo apt update
sudo apt install flatabulous-theme
sudo apt install ultra-flat-icons
sudo apt install unity-tweak-tool
```
然后启动`unity-tweak-tool`,主题选择`Flatabulous`，图标选择`Ultra-flat`

### 安装CodeBlock
* 访问  https://launchpad.NET/~damien-moore/+archive/ubuntu/codeblocks-stable
* 找到页面上以“ppa:”开头加粗的那一段英文，比如这次就是“ppa:damien-moore/codeblocks-stable”
```shell
sudo add-apt-repository ppa:damien-moore/codeblocks-stable
sudo apt update
sudo apt install codeblocks  libwxgtk3.0-dev wx-common codeblocks-contrib
```
##### 无法输入中文或终端中文出现乱码
```shell
Settings->General Setting->Environment-Terminal to launch console programs下拉菜单改成gnome-terminal -t $TITLE -x
```

### 无法正常关机重启
方法1：系统设置-> 软件和更新->附加驱动->安装专有驱动->安装完后重启，笔者就是用这种方法解决的。

方法2：
```shell
sudo gedit /etc/modprobe.d/blacklist.conf
最下面添加下列内容
blacklist vga16fb
blacklist nouveau
blacklist rivafb
blacklist nvidiafb
blacklist rivatv
```
方法3：在关机或重启前用`sync`命令

### 系统提示/boot空间不够
```shell
uname -a    //查看内核信息
dpkg --get-selections|grep linux-image   过滤过期内核
sudo apt purge linux-image-4.4.0-66-generic 删掉内核
```
ps:千万不要删掉现在的内核，后果很严重

### 安装smplayer
```shell
sudo apt install smplayer
```

### 安装文泉驿微字体
```shell
sudo apt install ttf-wqy-microhei
```

### 安装苹果启动项
```shell
sudo apt install docky
```

### 安装Android Studio
* 翻墙去官网下载Android studio
* 将下载下来的文件解压到`home`目录
* 进入Android studio目录里面的`bin`目录
* 给`studio.sh`添加运行权限
```shell
chmod +x studio.sh
```
* 终端运行
```shell
sh studio.sh        // 这里千万不要加sudo
```
* 经过一系列的下载安装,在主页面选择`Configure →Create Desktop Entry →for all users`

### vim配置
##### 第一种：界面好看
```shell
curl https://j.mp/spf13-vim3 -L > spf13-vim.sh && sh spf13-vim.sh
```
##### 第二种：方便运行
* 将下列东西复制到`~/.vimrc`,然后就可以自动补全括号,**F5编译,F6运行**
* 当然也可以两种方法结合，在是用了第一种方法之后，记得先去`~/.vimrc`，将其中的`F5`,`F6`快捷键用`"`注释掉，然后再复制粘贴以下代码

```bash
inoremap ( ()<Esc>i
inoremap [ []<Esc>i
inoremap { {<CR>}<Esc>O
autocmd Syntax html,vim inoremap < <lt>><Esc>i| inoremap > <c-r>=ClosePair('>')<CR>
inoremap ) <c-r>=ClosePair(')')<CR>
inoremap ] <c-r>=ClosePair(']')<CR>
inoremap } <c-r>=CloseBracket()<CR>
inoremap " <c-r>=QuoteDelim('"')<CR>
inoremap ' <c-r>=QuoteDelim("'")<CR>

function ClosePair(char)
 if getline('.')[col('.') - 1] == a:char
 return "<Right>"
 else
 return a:char
 endif
endf

function CloseBracket()
 if match(getline(line('.') + 1), 's*}') < 0
 return "<CR>}"
 else
 return "<Esc>j0f}a"
 endif
endf

function QuoteDelim(char)
 let line = getline('.')
 let col = col('.')
 if line[col - 2] == "\"
 return a:char
 elseif line[col - 1] == a:char
 return "<Right>"
 else
 return a:char.a:char."<Esc>i"
 endif
endf



" F6运行C
func! CompileGcc()
    exec "w"
    let compilecmd="!gcc "
    let compileflag="-o %< "
    if search("mpi.h") != 0
        let compilecmd = "!mpicc "
    endif
    if search("glut.h") != 0
        let compileflag .= " -lglut -lGLU -lGL "
    endif
    if search("cv.h") != 0
        let compileflag .= " -lcv -lhighgui -lcvaux "
    endif
    if search("omp.h") != 0
        let compileflag .= " -fopenmp "
    endif
    if search("math.h") != 0
        let compileflag .= " -lm "
    endif
    exec compilecmd." % ".compileflag
endfunc
func! CompileGpp()
    exec "w"
    let compilecmd="!g++ "
    let compileflag="-o %< "
    if search("mpi.h") != 0
        let compilecmd = "!mpic++ "
    endif
    if search("glut.h") != 0
        let compileflag .= " -lglut -lGLU -lGL "
    endif
    if search("cv.h") != 0
        let compileflag .= " -lcv -lhighgui -lcvaux "
    endif
    if search("omp.h") != 0
        let compileflag .= " -fopenmp "
    endif
    if search("math.h") != 0
        let compileflag .= " -lm "
    endif
    exec compilecmd." % ".compileflag
endfunc

func! RunPython()
        exec "!python %"
endfunc
func! CompileJava()
    exec "!javac %"
endfunc


func! CompileCode()
        exec "w"
        if &filetype == "cpp"
                exec "call CompileGpp()"
        elseif &filetype == "c"
                exec "call CompileGcc()"
        elseif &filetype == "python"
                exec "call RunPython()"
        elseif &filetype == "java"
                exec "call CompileJava()"
        endif
endfunc

func! RunResult()
        exec "w"
        if search("mpi.h") != 0
            exec "!mpirun -np 4 ./%<"
        elseif &filetype == "cpp"
            exec "! ./%<"
        elseif &filetype == "c"
            exec "! ./%<"
        elseif &filetype == "python"
            exec "call RunPython"
        elseif &filetype == "java"
            exec "!java %<"
        endif
endfunc

map <F5> :call CompileCode()<CR>
imap <F5> <ESC>:call CompileCode()<CR>
vmap <F5> <ESC>:call CompileCode()<CR>

map <F6> :call RunResult()<CR>
```
### 安装Xmind
* 官网下载：http://www.xmind.net/download/previous/
* `dpkg -i 包名`

### 安装indicator-sysmonitor
```shell
sudo add-apt-repository ppa:fossfreedom/indicator-sysmonitor
sudo apt update
sudo apt install indicator-sysmonitor
```
终端执行：`indicator-sysmonitor &`
为程序添加开机启动！鼠标右键点击标题栏上图标，弹出菜单，选择首选项  勾上`Run on startup`:， 这样就能开机启动了。切换到 Advanced 选项，可以对要显示的信息的格式进行设置。然后关闭终端,按window键搜索`indicator`,然后打开就行

### win10,Ubuntu双系统,发现window的盘打不开
类似这样的错误:`Error mounting /dev/sda5`
```shell
sudo ntfsfix /dev/sda5
```

### 安装GIMP
* 号称Linux下的ps
```shell
sudo apt install gimp
```

### 安装护眼的f.lux
```shell
sudo add-apt-repository ppa:nathan-renniewaldock/flux
sudo apt update
sudo apt install fluxgui
```

### 安装MPV播放器
* 相对于smplayer的另一个播放器
```shell
sudo add-apt-repository ppa:mc3man/mpv-tests
sudo apt update
sudo apt install mpv
```

### 提高笔记本电池寿命
```shell
sudo apt install tlp tlp-rdw
sudo tlp start
```

### 设置root密码
```shell
sudo su -
输入你的账户的密码
passwd
输入新的root密码
再次输入新的root密码
```

### 安装Qt
* 网站: https://www.qt.io/download-open-source/
选择不联网的那个
**安装的时候不要提权**
##### 安装Qt出现无法输入中文
1.安装fcitx-frontend-qt5
```shell
sudo apt install fcitx-frontend-qt5
```
2.输入`dpkg -L fcitx-frontend-qt5`,找到安装路径
,出现`libfcitxplatforminputcontextplugin.so`的就是
3.将上面的文件复制到Qt安装目录,我的是
```bash
/home/hua/Qt5.11.1/Tools/QtCreator/lib/Qt/plugins/platforminputcontexts
/home/hua/Qt5.11.1/5.11.1/gcc_64/plugins/platforminputcontexts
```

```bash
# 所以我的命令如下
cp -r /usr/lib/x86_64-linux-gnu/qt5/plugins/platforminputcontexts/libfcitxplatforminputcontextplugin.so /home/hua/Qt5.11.1/Tools/QtCreator/lib/Qt/plugins/platforminputcontexts
cp -r /usr/lib/x86_64-linux-gnu/qt5/plugins/platforminputcontexts/libfcitxplatforminputcontextplugin.so /home/hua/Qt5.11.1/5.11.1/gcc_64/plugins/platforminputcontexts
```

```bash
# 有时候可能有对`.so`文件进行提权，可`cd`到指定目录下，分别进行如下操作，如果提示没有权限就用`sudo`
chmod +x libfcitxplatforminputcontextplugin.so
chmod 777 libfcitxplatforminputcontextplugin.so
```

### 常用压缩包的打包和解压
* .tar.bz
 * 解压:`tar jxvf 文件名.tar.bz`
* .tar.gz
 * 解压:`tar zxvf 文件名.tar.gz`
 * 压缩:`tar zcvf 文件名.tar.gz 目标名`
* .zip:
 * 解压:`unzip -O CP936 xxx.zip`
 * 压缩:`zip 目标文件名.zip 要压缩的东西`,一般都是`zip 目标文件名.zip ./*`:将当前目录下的所有东西全部压缩成 目标文件名.zip

* .tar:
 * 解压:`tar xvf 文件名.tar`
 * 压缩:`tar cvf 文件名.tar 目标名`
* .rar:
 * 解压:`rar x 文件名.rar`
 * 压缩:`rar a 文件名.rar 目标名`

### 安装QQ
* 网站:http://phpcj.org/wineqq
* 准备环境
```shell
sudo add-apt-repository ppa:wine/wine-builds
sudo apt update
sudo apt install winehq-devel
```
* 下载wineqq
[下载地址](https://pan.baidu.com/s/1o8CotQU#list/path=%2F)
提取密码:f2sn
* 将压缩包解压到用户主目录
```shell
tar xvf wineQQ8.9.4_21584.tar.xz -C ~/
```
* 打开qq,等待安装一些东西即可
* 出现方块字体
```shell
PC:~winecfg//第一次运行然系统初始化好然后关闭下载好我给你们的文件（3个文件：wine−zh−fix−reg.tar.gz解压后放在一边在终端里面输入：‘PC: winecfg//第一次运行然系统初始化好然后关闭下载好我给你们的文件（3个文件：wine−zh−fix−reg.tar.gz解压后放在一边在终端里面输入：‘PC:  regedit xxx.reg //xxx.reg是解压的文件 全部都要执行该命令`
再打开wine：完美解决
```

##### 使用CrossOver安装qq
1.下载安装CrossOver
```shell
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install gdebi
wget http://crossover.codeweavers.com/redirect/crossover.deb
sudo gdebi crossover.deb
```

下载后解压出crack文件夹里面的`winewrapper.exe.so`
拷贝到`/opt/cxoffice/lib/wine/`目录下

##### 最简单的qq安装
* https://github.com/askme765cs/Wine-QQ-TIM
* 下载完成后,双击运行

### Atom配置
##### 相关设置
* Tab长度：File > settings > Tab Length 设置为4
##### 快捷键
* ctrl+shift+M：Markdown编辑环境下的分隔到右侧预览效果
##### 插件安装
* File > settings > Install > Search pachages >Packages >Install
* 安装完成后会在settings > Packages > Community Packages中看到
##### 插件介绍
* simplified-chinese-menu：简体中文包汉化菜单插件
* file-icons:file文件图标
* linter:检查错误
* minimap:小地图
* script:运行代码。快捷键`Ctrl+Shift+b`
* autocomplete-python:python代码自动补全
* highlight-selected:高亮选择的词
* minimap-highlight-selected:小地图高亮
* nucleus-dark-ui | seti-ui:最漂亮的两个主题
* atom-monokai | monokai:最漂亮的两个语法主题
* markdown-img-paste:图片粘贴(Ctrl+shift+v)
* markdown-preview-enhanced:中国人自己写的强大的markdown
* gpp-compiler:写C语言用


### ubuntu16.04与windows时间同步代码：
第一种方法
```shell
sudo timedatectl set-local-rtc 1 --adjust-system-clock
sudo timedatectl set-ntp 0
```
第二种方法
```shell
sudo apt install ntpdate
sudo ntpdate time.windows.com
sudo hwclock --localtime --systohc
```

### 出现“无法获得锁 /var/lib/apt/lists/lock"错误
```shell
sudo rm /var/lib/apt/lists/lock
```

### Gparted
* 一个分区工具，它可以用于创建、删除、移动分区，调整分区大小，检查、复制分区等操作。可以用于调整分区以安装新操作系统、备份特定分区到另一块硬盘等。
```shell
sudo apt install gparted -y
```

### FileZilla
* FileZilla是一个免费开源的FTP软件，分为客户端版本和服务器版本，具备所有的FTP软件功能。可控性、有条理的界面和管理多站点的简化方式使得Filezilla客户端版成为一个方便高效的FTP客户端工具。
```shell
sudo apt install filezilla
```

### Kazam
* Kazam 是 Ubuntu 上一款简易的桌面屏幕录制工具，它只能录制整个屏幕，可以录制声音，并可以快速上传录制好的视频到 YouTube 及 VideoBin 视频分享网站上

```shell
sudo add-apt-repository ppa:and471/kazam-daily-builds
sudo apt update
sudo apt install kazam
```

### Silentcast
* Silentcast是一款专注于GIF录制工具。

```shell
sudo add-apt-repository ppa:sethj/silentcast
sudo apt update
sudo apt install silentcast
```

### Okular
* Okular 是一个 PDF 文档阅读软件，支持 PDF、TIFF、CHM、ODF、EPUB、mobi 等文档格式。

```shell
sudo apt install okular -y
```

### Albert Spotlight
* Albert Spotlight是 Ubuntu的一项快速、随打即找、系统支援的桌面搜寻特色。spotlight 被设计为可以找到任何位于电脑中广泛的项目，包含文件、图片、音乐、应用程式、系统喜好设定控制台，也可以是文件或是PDF中指定的字。优雅地取代了Mac中的mac Spotlight。
* 在安装完成之后,打开,配置打开的快捷键即可.
* 民间
```shell
sudo add-apt-repository ppa:noobslab/macbuntu
sudo apt update
sudo apt install albert
```
* 官方
```shell
wget -nv https://download.opensuse.org/repositories/home:manuelschneid3r/xUbuntu_16.04/Release.key -O Release.key
sudo apt-key add - < Release.key
sudo sh -c "echo 'deb http://download.opensuse.org/repositories/home:/manuelschneid3r/xUbuntu_16.04/ /' > /etc/apt/sources.list.d/albert.list"
sudo apt update
sudo apt install albert
```

### enca
* enca文件编码转换工具。

```shell
sudo apt install enca
```
```
#enca查看文件编码
enca filename
```
### Figlet
* Figlet是一个将字符串在终端生成一个logo的终端工具。

```shell
sudo apt install figlet
```

### Wingware
* 这是一个很牛的PythonIDE
* 官网地址:http://www.wingware.com/
* Pro版本为商业版本,可[破解](http://blog.csdn.net/u011128775/article/details/70140255)
* 破解脚本,注意修改里面的LicenseID和RequestCode即可
```python
#!/usr/bin/env python3
LicenseID='CN823-12345-12345-67891'
RequestCode='RL625-QV8EM-EHT8Y-G5XW8'
import hashlib
B16 = '0123456789ABCDEF'
B30 = '123456789ABCDEFGHJKLMNPQRTVWXY'
def B(n,f,t):
  xx = 0
  for d in str(n):
    xx = xx * len(f) + f.index(d)
  res = ''
  while xx > 0:
    res=t[int(xx%len(t))]+res
    xx//=len(t)
  return res
def S(D):
  r = B(''.join([c for i,c in enumerate(D) if i//2*2==i]),B16,B30)
  while len(r) < 17:
    r = '1' + r
  return r
def A(c):
  return c[:5]+'-'+c[5:10]+'-'+c[10:15]+'-'+c[15:]
h = hashlib.sha1()
h.update(RequestCode.encode('utf-8')+LicenseID.encode('utf-8'))
lichash=A(RequestCode[:3]+S(h.hexdigest().upper()) )
data=[23,161,47,9]
tmp=0
realcode=''
for i in data:
  for j in lichash:
    tmp=(tmp*i+ord(j))&0xFFFFF
  realcode+=format(tmp,'=05X')
  tmp=0
D=B(realcode,B16,B30)
while len(D) < 17:
  D = '1' + D
print("The Activation Code is: "+A('AXX'+D))
```
* 在Ubuntu下无法输入中文
```
dpkg -L fcitx-frontend-qt5
```

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530168377.jpg)

```
dpkg -L wingide6 | grep platforminputcontexts
```

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530168371.jpg)

```
sudo cp /usr/lib/x86_64-linux-gnu/qt5/plugins/platforminputcontexts/libfcitxplatforminputcontextplugin.so  /usr/lib/wingide6/bin/runtime-qt5.5/plugins/platforminputcontexts
```
* 常用技巧
 * F1,F2:上下左右框的开合
 * Edit->Preferences->User Interface->Color Palete选择主题
 * 显示行号:Edit -> Show(Hide) Line Numbers
 * TAB:自动补全
 * 设置补全键：Edit->Keybord Personality->Config auto..->Editors->Auto-completion

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530168350.jpg)

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530168339.jpg)

### 安装汇编环境
```shell
sudo apt install dosemu
# 将下载下来dos程序如masm复制到`~/.dosemu/drives/d/bin`中即可
```
##### 编写汇编代码
1. 在dos下直接输入`edit`,用鼠标选择`File->New`,开始编写,然后选择`Save as`保存为`.asm`后缀文件即可
2. 终端进入`~/.dosemu/drives/c`目录下,用vim编写



### 开机自动挂载Windows分区
1. 前期准备
* 查看系统磁盘号
```shell
sudo fdisk -l
```
![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530168282.jpg)

* 查看磁盘类型
```shell
sudo blkid
```

2. 修改配置文件
```shell
sudo gedit /etc/fstab
```
* 配置文件包括下面几项:

|内容|例子|
|-----|-----|
|分区定位|可以给磁盘号，UUID或LABEL，例如：/dev/sda2，UUID=6E9ADAC29ADA85CD或LABEL=software |
|具体挂载点的位置|例如：/media/C |
|挂载磁盘类型|linux分区一般为ext4，windows分区一般为ntfs|
|挂载参数|一般为defaults|
|磁盘备份|默认为0，不备份|
|磁盘检查|默认为0，不检查|

* 配置图如下:

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1530168314.jpg)

```shell
# disk for Window10

# c for Windows10
UUID="3C5002DB50029BB0" /media/hua/3C5002DB50029BB0 ntfs    defaults    0   0

# d for Windows10
UUID="1C963ACF963AA962" /media/hua/软件安装处    ntfs    defaults    0   0

# e for Windows10
UUID="5CA074DBA074BD58" /media/hua/资料与娱乐    ntfs    defaults    0   0

# f for Windows10
UUID="4AD483BBD483A7B1" /media/hua/软件   ntfs    defaults    0   0

# g for Windows10
UUID="32C290FDC290C68F" /media/hua/虚拟机及代码   ntfs    defaults    0   0
```
3. 检查并挂载新添加项:
```shell
sudo mount -a
```
* 改命令会在`/etc/fstab`中的项全部挂载,如果有错,则会提示错误,然后根据错误找出原因修改

### 安装wireshark
* wireshark是一个网络抓包分析工具
```shell
sudo apt install wireshark    # 弹框选"YES"
sudo usermod -a -G wireshark $USER
```

### 为重装系统做准备
在自己的系统配置到差不多的时候，可以
```shell
sudo apt-mark showmanual > .install
```
在需要重装系统的时候，执行
```shell
sudo apt install $(cat .install)
```
就可以安装之前选择的所有软件了～
当然/home需要单独分区


### xx-net的ipv6
```shell
sudo apt install miredo
重启
sudo miredo
```

# 打开启动应用管理
```shell
gnome-session-properties
```
