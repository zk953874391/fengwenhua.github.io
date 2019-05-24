---
title: sqli-lab之第零章 环境搭建
mathjax: true
date: 2019-05-22 22:13:35
tags: 
- sqli-lab环境搭建
categories: 
- 渗透测试
- sqli-lab
---

## 前言
本系列教程的试验靶场为`sqli-labs` ,该靶场的下载地址为 https://github.com/Audi-1/sqli-labs ,可以自行去下载,而装了`git`的童鞋也可以直接用下面的命令clone到随意的目录

```
git clone https://github.com/Audi-1/sqli-labs
```

因为写这个靶场的印度程序猿当年的php的版本小于7,用的是类似于`mysql_`的语句,而现在的php都是用类似于`mysqli_`.因此,如果现在搭建的环境使用的php版本大于7就会报错

接下来会从win10, docker下讨论该环境怎么搭建

<!--more-->
## Windows
> windows下推荐使用`phpstudy`,当然`wamp`也可以,只不过phpstudy更加方便,可以去这里下载安装: http://phpstudy.php.cn/

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20181218112400.png)

下载完成之后,我的phpstudy是安装在`D:\phpStudy`

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20181218112748.png)

然后打开phpstudy,类似如下界面,

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20181218112942.png)

以下就是phpstudy启动成功的样子,两个大大的"绿点"

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.m6vjtgqeebm_1534071178.png)

phpStudy安装好之后, 将下载下来的`sqli-labs`复制到`WWW`文件夹下

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.6l5kfuyf925_1534071183.png)

编辑`sql-connections/db-creds.inc`文件，添加Mysql密码, 我这里设置成为`root`

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.qtzh4ztrf7r_1534071191.png)

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.nfdl7jzf3uj_1534071200.png)

并且在phpstudy中修改MYSQL的密码为一致（默认密码为`root`）

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.p8abdukyfkh_1534071211.png)

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.yrae1htj1s_1534071218.png)

打开网址`http://localhost/sqli-labs/`访问`Setup/resetDatabase for labs`

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.fw07042j06k_1534071230.png)

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.mo2c6g9a21_1534071236.png)

安装完成之后就可以开始学习之旅了！

## docker可视化版
> 对于linux和mac下, 本人极力推荐使用`docker`, 因为其本身环境配置过于麻烦, 所以这里只讨论docker的安装与配置~~

### kali
1. 增加Docker pgp key

    ```
    apt update
    apt install -y apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
    ```

2. 添加docker-ce的apt 源

    ```
    echo 'deb https://download.docker.com/linux/debian stretch stable' > /etc/apt/sources.list.d/docker.list
    apt update
    ```

3. 删除原系统docker

    ```
    apt purge docker docker-engine docker.io
    ```

4. 安装docker

    ```
    apt install docker-ce
    ```

5. 验证是否安装成功

    ```
    docker run hello-world
    ```

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190522124652.png)

6. 接下来安装`kitematic`, 去 https://github.com/docker/kitematic/releases 下载Ubuntu版本的

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190522124704.png)

    然后解压, 安装

    ```
    unzip Kitematic-0.17.7-Ubuntu
    cd Kitematic-0.17.7-Ubuntu/
    dpkg -i Kitematic-0.17.7_amd64.deb
    apt install -f
    ```

7. 然后打开`kitematic`, 输入账号密码登录一波, 然后搜索`sqli-labs`, 找到`acgpiano`, 点击`CREATE`即可

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190522124726.png)

8. 接下来就是打开sqli-lab了, 直接点`WEB PPREVIEW`右边那个按钮

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190522124750.png)

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190522124812.png)

9. 然后就是点击`Setup/reset Database for labs`, 初始化数据库, 操作与windows相同.

### mac下
#### 白果或者intel黑苹果
> mac下的安装就非常简单了

1. 下载安装[docker](https://hub.docker.com/editions/community/docker-ce-desktop-mac)
2. 下载安装[kitematic](https://github.com/docker/kitematic/releases)
3. 接下来就是打开kitematic, 操作步骤同上

#### amd黑苹果
> 好吧, 本人是个穷人, 没钱用白果, 所以只能靠hackintosh过日子了, 因为是amd黑苹果, 所以安装步骤略微复杂一些

amd 的docker无法正常工作, 解决链接: [https://forum.amd-osx.com/viewtopic.php?f=24&t=3543&p=45524&hilit=docker#p45524](https://forum.amd-osx.com/viewtopic.php?f=24&t=3543&p=45524&hilit=docker#p45524)

1. 下载安装virtualbox, 并打开, 确保其可以正常工作
2. 下载安装`Docker Toolbox for mac`, [https://github.com/docker/toolbox/releases](https://github.com/docker/toolbox/releases)
3. 下载安装`docker`
4. 打开终端

```
docker-machine create -d "virtualbox" --virtualbox-no-vtx-check --engine-install-url https://github.com/boot2docker/boot2docker/releases/download/v18.09.3/boot2docker.iso default
```

5. 打开[kitematic](https://github.com/docker/kitematic/releases), 接下来的步骤同上

## docker命令行版
> 如果你发现你安装的kitematic无法正常工作, 那没办法, 只能用命令行了

1. 拉取`sqli-labs`镜像

    ```
    docker pull acgpiano/sqli-labs
    ```

2. 运行该镜像

    ```
    docker run -dt --name SQLI-LABS -p 80 --rm  acgpiano/sqli-labs
    #run 创建一个新的容器并运行一个命令
    #-d 表示后台运行,返回容器id
    #-t  为容器重新分配一个伪输入终端，通常与 -i 同时使用
    #--name SQLI-LABS 将容器命名为SQLI-LABS
    #-p 80  将acgpiano/sqli-labs的80端口映射到本地的PORT端口
    ```

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/截图_1538711152)

    访问`localhost:32769`就可以看到效果了

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/截图_1538711194)

3. 进入docker镜像终端

    ```
    docker ps    # 查看正在运行的容器
    docker ps -a # 查看所有容器
    docker exec -it ID /bin/bash
    #exec 在运行的容器中执行命令
    #-t 分配一个伪终端
    #-i 即使没有附加也保持STDIN 打开(不懂)
    ```

4. docker常用命令

    ```
    docker images                 # 列出本地镜像
    docker start CONTAINER        # 启动一个或多少已经被停止的容器
    docker stop CONTAINER         # 停止一个运行中的容器
    docker restart CONTAINER      # 重启容器
    docker rm CONTAINER           # 删除容器
    docker rmi IMAGE              # 删除镜像
    sudo systemctl daemon-reload  # reload daemon.json
    sudo systemctl restart docker # 重启docker
    ```


## 给sqli-lab安装vim
为了方便修改文件, 所以我们需要安装vim, 但是官方源已经挂了, 所以, 我们需要添加[清华源](https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/)

`vi`修改`/etc/apt/sources.list`如下

```
vi /etc/apt/sources.list
```

```
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ trusty main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ trusty-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ trusty-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ trusty-security main restricted universe multiverse
```

然后需要解决https的问题

```
cd /usr/lib/apt/methods
ln -s http https

apt-get update
apt-get install apt-transport-https
```

最后安装vim即可
```
apt install vim
```
