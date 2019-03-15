---
title: web源码泄露总结
date: 2019-03-10 21:38:21
tags: 
- web源码泄露
categories: 
- 渗透测试
---

### 参考
https://www.xmanblog.net/2017/04/03/web-code-leakage/

## 寻找源代码备份
> 在打ctf的时候,有时候页面什么提示都没有,这时候就要考虑一下是不是源代码泄露了

### hg 源码泄露
`hg init` 时会产生 `.hg` 文件。

```
# 可以通过以下链接访问
http://www.example.com/.hg/
```
[利用工具 dvcs-ripper](https://github.com/kost/dvcs-ripper)
```
rip-hg.pl -v -u http://www.example.com/.hg/
```
<!--more-->
### Git 源码泄露
在运行`git init`初始化代码库的时候，会在当前目录下面产生一个`.git`的隐藏文件，用来记录代码的变更记录等等。在发布代码的时候，如果`.git`这个目录没有删除，直接发布了。使用这个文件，可以用来恢复源代码。
```
# 可以通过以下链接访问
http://www.example.com/.git
http://www.example.com/.git/HEAD
http://www.example.com/.git/index
http://www.example.com/.git/config
http://www.example.com/.git/description
```

#### 漏洞利用
* [GitHack](https://github.com/lijiejie/GitHack)
```
python GitHack.py http://www.example.com/.git/
```

* [GitHacker（可恢复完整 Git 仓库）](https://github.com/WangYihang/GitHacker)
```
python GitHacker.py http://www.example.com/.git/
```

* [dvcs-ripper](https://github.com/kost/dvcs-ripper)
```
rip-git.pl -v -u http://www.example.com/.git/
```

### .DS_Store 文件泄露
Mac OS 中会包含有 `.DS_Store` 文件，在发布代码时未删除文件夹中隐藏的`.DS_store`，被发现后，获取了敏感的文件名等信息.
```
# 可通过以下链接访问
http://www.example.com/.ds_store
```

#### 漏洞利用
[ds＿store＿exp](https://github.com/lijiejie/ds_store_exp)
```
python ds_store_exp.py http://www.example.com/.ds_store
```

### 网站备份压缩文件
在网站的使用过程中，往往需要对网站中的文件进行修改、升级。此时就需要对网站整站或者其中某一页面进行备份。**当备份文件或者修改过程中的缓存文件因为各种原因而被留在网站web目录下，而该目录又没有设置访问权限时**，便有可能导致备份文件或者编辑器的缓存文件被下载，导致敏感信息泄露，给服务器的安全埋下隐患。

常见的后缀名：
```
.rar
.zip
.7z
.tar
.tar.gz
.bak
.txt
.swp
.html
```

### SVN 泄露
`Subversion，简称SVN`，是一个开放源代码的版本控制系统，相对于的RCS、CVS，采用了分支管理系统，它的设计目标就是取代CVS。互联网上越来越多的控制服务从CVS转移到Subversion。

Subversion使用`服务端—客户端`的结构，当然服务端与客户端可以都运行在同一台服务器上。在服务端是存放着所有受控制数据的Subversion仓库，另一端是Subversion的客户端程序，管理着受控数据的一部分在本地的映射（称为“工作副本”）。在这两端之间，是通过各种仓库存取层（Repository Access，简称RA）的多条通道进行访问的。**这些通道中，可以通过不同的网络协议，例如HTTP、SSH等，或本地文件的方式来对仓库进行操作**。

```
# 可通过以下链接访问
http://vote.lz.taobao.com/admin/scripts/fckeditor.266/editor/.svn/entries
```

敏感文件：
```
/.svn
/.svn/wc.db
/.svn/entries
```
#### 漏洞利用
* [dvcs-ripper](https://github.com/kost/dvcs-ripper)
```
perl rip-svn.pl -v -u http://www.example.com/.svn/
```
* [Seay - SVN](http://tools.40huo.cn/#!web.md#%E6%BA%90%E7%A0%81%E6%B3%84%E9%9C%B2)

### WEB-INF / web.xml 泄露
WEB-INF 是 Java Web 应用的安全目录，如果想在页面中直接访问其中的文件，必须通过`web.xml`文件对要访问的文件进行`相应映射`才能访问。

WEB-INF 主要包含一下文件或目录：
* /WEB-INF/web.xml ：Web 应用程序配置文件，描述了 servlet 和其他的应用组件配置及命名规则。
* /WEB-INF/classes/ ：含了站点所有用的 class 文件，包括 servlet class 和非 servlet class，他们不能包含在.jar 文件中。
* /WEB-INF/lib/ ：存放 web 应用需要的各种 JAR 文件，放置仅在这个应用中要求使用的 jar 文件，如数据库驱动 jar 文件。
* /WEB-INF/src/ ：源码目录，按照包名结构放置各个 java 文件。
* /WEB-INF/database.properties ：数据库配置文件。

#### 漏洞成因
通常一些web应用我们会使用多个web服务器搭配使用，解决其中的一个web服务器的性能缺陷以及做均衡负载的优点和完成一些分层结构的安全策略等。在使用这种架构的时候，由于对静态资源的目录或文件的映射配置不当，可能会引发一些的安全问题，导致web.xml等文件能够被读取。

#### 漏洞检测及利用方法
通过找到 web.xml 文件，推断 class 文件的路径，最后直接 class 文件，在通过反编译 class 文件，得到网站源码。 一般情况，jsp 引擎默认都是禁止访问 WEB-INF 目录的，Nginx 配合 Tomcat 做均衡负载或集群等情况时，问题原因其实很简单，Nginx 不会去考虑配置其他类型引擎（Nginx 不是 jsp 引擎）导致的安全问题而引入到自身的安全规范中来（这样耦合性太高了），修改 Nginx 配置文件禁止访问 WEB-INF 目录就好了：
```
location ~ ^/WEB-INF/* { deny all; } # 或者return 404; 或者其他！
```

### CVS 泄露
```
http://url/CVS/Root 返回根信息
http://url/CVS/Entries 返回所有文件的结构
```

取回源码的命令
```
bk clone http://url/name dir
```

这个命令的意思就是把远端一个名为`name`的`repo` clone到本地名为`dir`的目录下。

查看所有的改变的命令，转到download的目录
```
bk changes
```

### Bazaar/bzr
[dvcs-ropper](https://github.com/kost/dvcs-ripper)
```
rip-bzr.pl -v -u http://www.example.com/.bzr/
```

#### 工具推荐
* [Bitkeeper](http://www.bitkeeper.com/installation.instructions)
* [weakfilescan](https://github.com/ring04h/weakfilescan)

