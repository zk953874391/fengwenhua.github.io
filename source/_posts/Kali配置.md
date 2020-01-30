---
title: Kali配置
date: 2018-11-15 15:18:18
mathjax: true
tags:
- kali显卡
- kali系统安装
- kali安装 ss-qt5
categories:
- Linux
- Kali
---


## 系统安装
> 据博主亲测,Kali从2018年版本开始,再用`UltraISO`之类的软件制作U盘启动盘来装Kali系统,都会出现下图的问题,百度和google上有很多解决方案,然并卵.

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1529331889.jpg)

今天偶然发现了一款U盘制作软件---`Rufus`,可以去[官网](https://rufus.akeo.ie/) 下载,在用`Rufus`制作启动U盘的时候,选择后U盘和Kali的安装文件,点击`开始`,这时候只要选择如下图的`DD`模式,就会正常安装Kali了.

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1529332318.jpg)
<!-- more -->
## 软件安装

### 1. shadowsocks-qt5
> 身在华夏,当然免不了被墙,而Kali的官方源是国外的服务器,所以,那速度...无法忍受,当然,也可以用国内的源,然后,博主的强迫症发作,因此决定用`ss-qt5`出去溜达溜达!说起来,现在连`ss-qt5`都用`Appimage`这种跨平台的打包方式,我喜欢...

#### 1. [github](https://github.com/)搜索`shadowsocks-qt5`->`releases`->找到对应执行程序(Appimage)下载即可

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1529336937.jpg)

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1529337025.jpg)

#### 2. 可以说,所有的Appimage程序都是用以下的方式运行的
```shell
chmod +x Shadoosocks-Qt5-3.0.1-x86_64.AppImage
```

#### 3. 双击运行,然后加入你服务器的配置就行

#### 4. 配置终端fq
> 终端不支持socks5协议,所以需要借助工具`proxychains4`

```
git clone https://github.com/rofl0r/proxychains-ng.git
cd proxychains-ng
./configure --prefix=/usr --sysconfdir=/etc
make
sudo make install
sudo make install-config
sudo gedit /etc/proxychains4.conf

```


### 2. 显卡驱动
> 装完Kali,当然得装显卡不懂啊,不然排热扇猛地在转,笔记本很快就没电了.
> 注意:在安装显卡之前,必须要更新完系统,命令如下

```shell
apt update
apt upgrade -y
apt dist-upgrade -y
```

#### 1. 安装 Linux 内核头
通过命令`uname -a`查看自己的内核版本
```shell
apt install linux-headers-4.15.0-kali2-amd64 linux-headers-4.15.0-kali2-common linux-headers-4.15.0-kali2-all
```
> ps:如果实在没有,可以试试`apt install linux-headers-*`全部安装


#### 2. 禁用默认使用的显卡驱动 `nouveau`。在命令行中输入
```shell
echo -e "blacklist nouveau\noptions nouveau modeset=0\nalias nouveau off" > /etc/modprobe.d/blacklist-nouveau.conf
```
应用刚刚的修改并重启系统
```shell
update-initramfs -u && reboot
```

#### 3. 重启后 `nouveau` 应该被禁用了。在命令行中输入以下命令来确认 `nouveau` 被禁用
```shell
lsmod |grep -i nouveau
```
如果输入此命令后**未显示任何内容**，证明 `nouveau` 已被成功禁用。

#### 4. 下载 NVIDA 官方驱动
到 NVIDA 的官网下载对应型号的驱动 http://www.nvidia.com/Download/index.aspx?lang=en-us ，注意，这里要选择和你显卡硬件型号对应的版本，否则一定失败。比如我的是 `GTX960M` 的笔记本显卡，所以我的选择如下图：

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1529338402.jpg)

点击`SEARCH` 后就可以看到 `DOWNLOAD` 的按钮了，点击下载就可以了

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/1529338471.jpg)

#### 5. 安装
下载好 NVIDA 的显卡驱动文件后，使用以下命令赋予执行权限
```shell
chmod a+x NVIDIA-Linux-x86_64-390.67.run
```

然后使用以下命令安装.注意,**安装过程中会提示警告，全部选择 `yes`**。
```shell
./NVIDIA-Linux-x86_64-384.98.run
```

#### 6. 配置
安装完成之后,必须要配置一些东西,**让Kali知道你使用的是什么显卡驱动**,否则可能开机黑屏.

##### 1. 查看显卡`BusID`
```
nvidia-xconfig --query-gpu-info | grep 'BusID : ' | cut -d ' ' -f6
```
它应该会显示如下的内容
```
PCI:2:0:0
```
这个就是我们需要的 **BUS ID**

##### 2. 创建一个 `/etc/X11/xorg.conf`文件
```shell
gedit /etc/X11/xorg.conf
```
然后填入以下内容

```shell
Section "ServerLayout"
Identifier "layout"
Screen 0 "nvidia"
Inactive "intel"
EndSection

Section "Device"
Identifier "nvidia"
Driver "nvidia"
BusID "PCI:2:0:0"
EndSection

Section "Screen"
Identifier "nvidia"
Device "nvidia"
Option "AllowEmptyInitialConfiguration"
EndSection

Section "Device"
Identifier "intel"
Driver "modesetting"
EndSection

Section "Screen"
Identifier "intel"
Device "intel"
EndSection
```
注意,**将`PCI:2:0:0`替换为自己的 `BUS ID`**，保存即可

#### 7. 据我们的显示管理器 (display manager)来创建一些脚本
由于我们的 kali 默认使用的是 `GDM (Gnome Display Manager)`，我们需要创建两个文件：
```shell
gedit /usr/share/gdm/greeter/autostart/optimus.desktop
gedit /etc/xdg/autostart/optimus.desktop
```
内容均为
```shell
[Desktop Entry]
Type=Application
Name=Optimus
Exec=sh -c "xrandr --setprovideroutputsource modesetting NVIDIA-0; xrandr --auto"
NoDisplay=true
X-GNOME-Autostart-Phase=DisplayServer
```

#### 8. 重启系统之后检测是否正常
```
apt install mesa-utils
glxinfo | grep -i "direct rendering"
```
如果一切正常,应当显示
```
direct rendering: Yes
```

#### 3. 安装输入法
1. 安装
```
apt install ibus ibus-pinyin fcitx fcitx-googlepinyin  ibus-setup
```
2. 选择输入法
```
Input Method->Add->汉语->pingyin
```
3. 输入源选择
```
设置->区域和语言->输入源->汉语->拼音
```

### 4. 坚果云
> 国内的`Dropbox`,不能不用啊!!!然而却没有合适Kali版本的,ubuntu和debian版本我都试过了,用不了,只能用源码了

```
apt install libglib2.0-dev libgtk2.0-dev libnautilus-extension-dev gvfs-bin openjdk-8-jre-headless
wget http://www.jianguoyun.com/static/exe/installer/nutstore_linux_src_installer.tar.gz
tar zxf nutstore_linux_src_installer.tar.gz
cd nutstore_linux_src_installer && ./configure && make
make install
nautilus -q
./runtime_bootstrap
```

### 5. root用户打开chrome
> 好吧!我也不知道为毛root用户打不开chrome

使用文件管理器打开路径`/usr/share/applications/` ，找到`google-chrome`的图标，鼠标右键打开属性，在命令一栏`/usr/bin/google-chrome-stable %U` 的后面加上`--no-sandbox --user-data-dir &`。
重新打开chrome即可

### 6. `终端`设置快捷键
设置->设备->键盘->命令如下:
```
gnome-terminal
```

### 7. 添加add-apt-repository
>  Kali Linux默认不含add-apt-repository，某些情况下并不方便。可以手动启用它来添加PPA。

* 首先安装软件属性程序包。
```shell
apt install software-properties-common
```
* 接下来安装`apt-file`。
```shell
apt install apt-file
```
* 更新`apt-file`。
```shell
apt-file update
```
* apt-file更新完毕，你应该能够搜索它了。
```shell
apt-file search add-apt-repository
```
* 你的输出结果应该看起来类似这样：
```
software-properties-common: /usr/bin/add-apt-repository
software-properties-common: /usr/share/man/man1/add-apt-repository.1.gz
```
* 模仿Ubuntu，让add-apt-repository正常工作。
```shell
cd /usr/sbin
gedit add-apt-repository
```
* 添加下列代码，并保存文件。
```bash
#!/bin/bash
if [ $# -eq 1 ]
NM=`uname -a && date`
NAME=`echo $NM | md5sum | cut -f1 -d" "`
then
  ppa_name=`echo "$1" | cut -d":" -f2 -s`
  if [ -z "$ppa_name" ]
  then
    echo "PPA name not found"
    echo "Utility to add PPA repositories in your debian machine"
    echo "$0 ppa:user/ppa-name"
  else
    echo "$ppa_name"
    echo "deb http://ppa.launchpad.net/$ppa_name/ubuntu xenial main" >> /etc/apt/sources.list
    apt-get update >> /dev/null 2> /tmp/${NAME}_apt_add_key.txt
    key=`cat /tmp/${NAME}_apt_add_key.txt | cut -d":" -f6 | cut -d" " -f3`
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys $key
    rm -rf /tmp/${NAME}_apt_add_key.txt
  fi
else
  echo "Utility to add PPA repositories in your debian machine"
  echo "$0 ppa:user/ppa-name"
fi
```
* **注意**：在`echo “deb http://ppa.launchpad.net/$ppa_name/ubuntu xenial main” >> /etc/apt/sources.list` 这一行中，我使用了xenial，也就是ubuntu 16.04。你可以根据自己的选择，更改其他代号。现在，使用`chmod`和`chown`这两个命令，对文件进行相应的操作。
```shell
chmod +x /usr/sbin/add-apt-repository
chown root:root /usr/sbin/add-apt-repository
```
接下来就可以使用`add-apt-repository`，添加PPA软件库。我试着输入下面这些命令，安装`ssqt5`。
```shell
add-apt-repository ppa:hzwhuang/ss-qt5
apt update
apt install shadowsocks-qt5
```


