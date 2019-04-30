---
title: python调用通知中心
date: 2018-11-30 21:18:18
mathjax: true
tags:
- mac系统通知
- 通知中心
- windows系统通知
- linux系统通知
- 系统提示
categories:
- Qt
---

## mac
> mac参考: https://stackoverflow.com/questions/17651017/python-post-osx-notification/41318195#41318195

### 法一:安装terminal-nofifier(推荐)
#### Ruby安装
```
sudo gem install terminal-notifier
```
<!--more-->
#### Homebrew安装
```
brew install terminal-notifier
```

#### 使用
* 所以用法看官网 https://github.com/julienXX/terminal-notifier

```python
import os


def notify(title, subtitle, message):
    '''调用系统提醒,即所谓的系统通知,需要安装terminal-notifier'''
    # 标题
    title = '-title {!r}'.format(title)
    # 子标题
    subtitle = '-subtitle {!r}'.format(subtitle)
    # 消息
    message = '-message {!r}'.format(message)
    # 默认提示音
    sound = '-sound default'
    # 自定义icon   -appIcon http://vjeantet.fr/images/logo.png
    os.system(
        'terminal-notifier {}'.format(' '.join([message, title, subtitle, sound])))


notify(title='标题',
       subtitle='子标题',
       message='内容')
```



### 法二:oaascript
> 该方法自定义图标以及添加提示音有点麻烦

1. 调用通知中心弹出消息

```
osascript -e 'display notification "内容" with title "标题"'
```

2. 调用某应用弹出消息

```
osascript -e 'tell app "Mail" to display dialog "该发周报了！" with title "提示"
```

其中Mail可以改为对应的app名称（非Launchpad上显示的名称，而是 ‘xxx.app’中’.app’前面的名称）

3. 然后在python中使用如下命令便可弹出提示

```python
import subprocess

title = "这个是标题"
content = "这个是内容"

# 执行AppleScripts命令， osascript -e 'display notification "内容" with title "标题"'
cmd = 'display notification "%s" with title "%s"' % (content, title)
subprocess.call(["osascript", "-e", cmd])
```

### 法三:ntfy
#### 安装

```
pip3 install ntfy
```

#### 使用
* 用法看官网: https://github.com/dschep/ntfy#backends
* 简单的python如下:

```python
import os


def notification(title, message):
    cmd = 'ntfy -t {0} send {1}'.format(title, message)
    os.system(cmd)


notification("title", "content")
```

### 法四:Foundation

```python
from Foundation import NSUserNotification
from Foundation import NSUserNotificationCenter
from Foundation import NSUserNotificationDefaultSoundName


class Notification():
    def notify(self, _title, _message, _sound=False):
        self._title = _title
        self._message = _message
        self._sound = _sound

        self.notification = NSUserNotification.alloc().init()
        self.notification.setTitle_(self._title)
        self.notification.setInformativeText_(self._message)
        if self._sound == True:
            self.notification.setSoundName_(NSUserNotificationDefaultSoundName)

        center = NSUserNotificationCenter.defaultUserNotificationCenter()
        center.deliverNotification_(self.notification)


N = Notification()
N.notify(_title="SOME", _message="Something", _sound=True)

```

## windows
> 用到`win10toast`

### 安装win10toast
```
pip3 install win10toast
```

### 使用
```python
from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("Hello world!!","Python is good")

# 详细用法
# duration=10代表10s后消失,改为-1则留在通知中心
toaster.show_toast("hello world!!","python is good",icon_path="custom.ico",duration=10)
```

## Linux
### 法一:notify-send

```
import os

title = "这个是标题"
content = "这个是内容"
# 执行命令notify-send -i [ icon ] <title>  [ message]
cmd = "sudo notify-send '%s' '%s'" % (title, content)
os.system(cmd)
```

### 法二:ntfy
* 具体用法参考在刚刚mac系统处已经说明

## pyqt自定义
* 脚本参考: https://github.com/kindlychung/PopupBubble

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-29 15:16:30
# @Author  : 江南小虫虫 (fwh13612265462@gmail.com)
# @Link    : http://www.fengwenhua.top
# @Version : $Id$


import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import base64
import traceback


class PopupBubble(QtWidgets.QDialog):
    def __init__(self, title, msg, duration=2):
        try:
            QtWidgets.QDialog.__init__(self)
            self.duration = duration
            self.title_label = QtWidgets.QLabel(self.make_bold(title))
            self.title_label.setWordWrap(True)
            self.title_label.setAlignment(QtCore.Qt.AlignCenter)
            self.msg_label = QtWidgets.QLabel(msg)
            self.msg_label.setWordWrap(True)
            self.icon_button = QLabelButton()
            img_b64 = "iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAITgAACE4BjDEA7AAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAABJdEVYdENvcHlyaWdodABQdWJsaWMgRG9tYWluIGh0dHA6Ly9jcmVhdGl2ZWNvbW1vbnMub3JnL2xpY2Vuc2VzL3B1YmxpY2RvbWFpbi9Zw/7KAAAB2ElEQVRIibWVPW/TUBiFz7mJTBFSGgnUqmABRgpMUYi53pCK1IWxUxd2BgYk/goDAzuq+AFILEhIZUuq/ACPrYRKGSJPdHkPQx3UOK7tJOKd7Guf57nXH++lJFRVr9e70el03pLcBnAnH/4t6SzLsvdpml5U5duVdABhGDLLsj6AjSvD9wFshWHIujzrVgBcrqLb7b6U9AoASH6aTqdf62YPAK6WDiBN0wszO52dm9lpEzhQs4LhcNhzzj13zj2TtDUXJH+Z2bGZ/ZhMJulSApL03r+WtNdoluS38Xj8USWw0kcUx/F+UzgASNqL43i/7NqCwHu/A+CgKfxKHeTZagGAPsnWsvQ8028ieLIsvCq7IJD0eFV6WXZO4L3fzFvCSkVy23u/ea2A5KNV4dcx5gRm9nBdQZFRfAcP1hUUGXMC59zagiLjn2AwGNwCsPCjrFA7OWteEATBrqRG3bWqJLkgCHZn523gsrnFcdwi+YXkrGEJAMxMs+OSonNutukwF9DMWiQpSUyS5Kmku+vOvKzM7KxtZu8A3PwfAgB/2iQ/m9m9qrtIxgBuF4bPJY1qBD8b7clJkryQ9KYg/TAajb7XZRt9NVEUHUk6BHAC4ETSYRRFR02yfwEMBLRPQVtfqgAAAABJRU5ErkJggg=="
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(base64.b64decode(img_b64))
            self.icon_button.setPixmap(pixmap)
            self.icon_button.resize(20, 20)

            title_layout = QtWidgets.QVBoxLayout()
            title_layout.addWidget(self.title_label)
            title_layout.addWidget(self.msg_label)
            layout = QtWidgets.QHBoxLayout()
            layout.addWidget(self.icon_button)
            layout.addLayout(title_layout, 1)
            self.setGeometry(0, 0, 300, 100)
            self.setLayout(layout)

            # self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            setWinBottomRight(self)
            QtCore.QTimer.singleShot(self.duration * 1000, self.close)
            self.installEventFilter(self)
        except:
            traceback.print_exc()
            # db.insert_error_log(phone="")

    def eventFilter(self, source, event):
        """label_path 鼠标点击事件"""
        try:
            if event.type() == QtCore.QEvent.MouseButtonPress:
                self.close()
            return QtWidgets.QWidget.eventFilter(self, source, event)
        except:
            traceback.print_exc()
            db.insert_error_log(phone=self.user_info["phone"])

    def make_bold(self, text):
        try:
            return "<b>" + text + "</b>"
        except:
            traceback.print_exc()
            db.insert_error_log(phone="")


class QLabelButton(QtWidgets.QLabel):
    def __init(self, parent):
        QLabel.__init__(self, parent)

    def mouseReleaseEvent(self, ev):
        self.emit(QtCore.SIGNAL('clicked()'))


def setWinBottomRight(app):
    br = QtWidgets.QDesktopWidget().availableGeometry().bottomRight()
    size = app.size()
    x = br.x() - size.width()
    y = br.y() - size.height()
    app.move(x, y)


def popup(title, msg, duration):
    app = QtWidgets.QApplication(sys.argv)
    toast = PopupBubble(title, msg, duration)
    toast.show()
    app.exec_()


if __name__ == "__main__":
    popup(title="这个是标题",
          msg="这个是内容!",
          duration=3)

```
