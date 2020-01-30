---
title: Kali 安装 jdk
date: 2020-01-26 19:26:43
tags:
- jdk
categories:
- Linux
- Kali
---

1. [官网](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)下载`jdk-linux-x64.tar.gz`

2. `tar -xvzf jdk-linux-x64.tar.gz`解压到当前目录

3. 然后复制到`/usr/jdk`

```bash
cp -r jdk1.8.0_201/ /usr/jdk
```

4. 编辑`/etc/profile`，加入如下命令以配置java的环境变量

复制以下内容追加到文件末尾

```bash
export JAVA_HOME=/usr/jdk
export CLASSPATH=.:$JAVA_HOME/lib:$JAVA_HOME/jre/lib:$CLASSPATH
export PATH=$JAVA_HOME/bin:$JAVA_HOME/jre/bin:$PATH
```

5. 告诉系统JDK的位置，最后2行代码不是重复，是要执行2次

```
update-alternatives --install "/usr/bin/java" "java" "/usr/jdk/bin/java" 1
update-alternatives --install "/usr/bin/javac" "javac" "/usr/jdk/bin/javac" 1
update-alternatives --install "/usr/bin/javaws" "javaws" "/usr/jdk/bin/javaws" 1
update-alternatives --install "/usr/bin/javaws" "javaws" "/usr/jdk/bin/javaws" 1
```

6.  设置新的JDK为默认,代码也是执行2次

```
update-alternatives --set java /usr/jdk/bin/java
update-alternatives --set java /usr/jdk/bin/java

update-alternatives --set javac /usr/jdk/bin/javac
update-alternatives --set javac /usr/jdk/bin/javac

update-alternatives --set javaws /usr/jdk/bin/javaws
update-alternatives --set javaws /usr/jdk/bin/javaws
```

7. `source /etc/profile`: 重载Profile文件
8. 输入`java -version`，看到如下图则说明配置成功

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190228121814.png)
