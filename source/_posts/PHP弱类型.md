---
title: PHP弱类型
date: 2019-03-10 22:16:20
tags: 
- php弱类型
categories: 
- 渗透测试
---


### 参考：
[PHP弱类型安全问题总结 | 乘物游心](https://blog.spoock.com/2016/06/25/weakly-typed-security/)

### PHP弱类型简介
* 在PHP中，可以进行以下的操作。

```php
$param = 1;
$param = array();
$param = "stringg";
```
<!--more-->
* **弱类型的语言对变量的数据类型没有限制**，你可以在任何地时候将变量赋值给任意的其他类型的变量，同时变量也可以转换成任意地其他类型的数据。

### 类型转换问题
* 类型转换是无法避免的问题。例如**需要将GET或者是POST的参数转换为int类型，或者是两个变量不匹配的时候，PHP会自动地进行变量转换**。但是PHP是一个弱类型的语言，导致在进行类型转换的时候会存在很多意想不到的问题。

#### 比较操作符

##### 类型转换
* 在`$a==$b`的比较中

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190310215030.png)

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190310215053.png)

* 这样的例子还有很多，这种比较都是相等。**PHP会把`类数值`(如含有数字的字符串等)的字符串转换为数值进行比较，如果参数是字符串，则返回字符串中第一个不是数字的字符之前的数字串所代表的整数值**
* 使用**比较操作符**的时候也存在类型转换的问题，如下：

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190310221503.png)

* 当**不同类型的变量进行比较的时候就会存在`变量转换`的问题**，在转换之后就有可能会存在问题。
* **当一个字符串当作一个数值来取值**，其结果和类型如下:
    * 如果该字符串没有包含`.`，`e`，`E`并且其数值值在`整型`的范围之内，该字符串被当作`int`来取值，其他所有情况下都被作为`float`来取值，该**字符串的`开始部分`决定了它的值**
    * 如果该字符串以合法的数值开始，则使用该数值，否则其值为0
    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190310221523.png)

* 这里需要注意一下，第二个条件是`===`，和`==`是有点区别的：
    * `===`是恒等计算符 同时检查表达式的值与类型,可以理解为**先检查类型再检查值**
    * `==`是比较运算符号 不会检查条件式的表达式的类型,**如果类型不同的进行比较，其会将类型转换成相同的再进行比较**

##### Hash比较
> kali中输入如下代码验证：`php -r 'var_dump("00e0345" == "0");'`
![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190310221542.png)

* 除了以上的这种方式之外在进行hash比较的时候也会存在问题。php在处理hash字符串的时候会用到`!=`,`==`来进行hash比较，**如果hash值以`0e`开头，后边都是`数字`，再与数字比较，就会被解释成	`科学记数法`:`0*10^n`还是为`0`，就会被判断相等**,如下：

```
"0e132456789"=="0e7124511451155" // true
"0e123456abc"=="0e1dddada"	       // false
"0e1234abc"=="0"  					 // false
```

* 当全是数字的时候，宽松的比较会执行**尽力模式**，如`0e12345678`会被解释成`0*10^12345678`, **除了`e`外不全是数字的时候就不会相等**

###### 例题
```php
<?php
error_reporting(0);
$flag = 'flag{test}';
if  ("POST" == $_SERVER['REQUEST_METHOD'])
{
    $password = $_POST['password'];
    if (0 >= preg_match('/^[[:graph:]]{12,}$/', $password)) 
    {
        echo 'Wrong Format';
        exit;
    }
    while (TRUE)
    {
        $reg = '/([[:punct:]]+|[[:digit:]]+|[[:upper:]]+|[[:lower:]]+)/'; 
        if (6 > preg_match_all($reg, $password, $arr)) 
            break;
        $c = 0;
        $ps = array('punct', 'digit', 'upper', 'lower'); 
        foreach ($ps as $pt)
        {
            if (preg_match("/[[:$pt:]]+/", $password)) 
                $c += 1;
        }
        if ($c < 3) break;
        if ("42" == $password) echo $flag;
        else echo 'Wrong password';
        exit;
    }
}
?>
```

* 这里的意思就是：接收post参数password的值，必须满足12位以上字符，必须是非空格非TAB之外的内容，然后就是你的password要有大小写数字，字符内容，而且匹配到的次数要大于6次，最后才是这里的考点：

```php
if ("42" == $password) echo $flag; 
else echo 'Wrong password';
```

* 最后的答案就是：`42.00e+00000000000 ` , 当然也可以这样：`420.000000000e-1`
* 42.00e+0000000000，10的00000次方。。等于42.000000…. 结果其实就是42

##### 十六进制转换
* 还存在一种十六进制余字符串进行比较运算时的问题。例子如下：

```
"0x1e240"=="123456"		// true
"0x1e240"==123456		   // true
"0x1e240"=="1e240"		// false
```

* 当其中的一个字符串是`0x`开头的时候，PHP会**将此字符串解析成为`十进制`然后再进行比较**，`0x1240`解析成为十进制就是`123456`，所以与**int类型和string类型的123456比较都是相等**。


#### 类型转换
常见的转换主要就是`int转换为string`，`string转换为int`。

##### int转string：
```
$var = 5;
方式1：$item = (string)$var;
方式2：$item = strval($var);
```

##### string转int：`intval()`函数。
* 对于这个函数，可以先看2个例子。

```php
var_dump(intval('2'))	//2
var_dump(intval('3abcd'))	//3
var_dump(intval('abcd'))	//0
```

* 说明`intval()`转换的时候，会将**从字符串的开始进行转换直到遇到一个`非数字`的字符**。即使出现无法转换的字符串，`intval()`不会报错而是**返回0**。
* 同时，程序员在编程的时候也不应该使用如下的这段代码：

```php
if(intval($a)>1000) {
    mysql_query("select * from news where id=".$a)
}
```
这个时候`$a`的值有可能是`1002 union…..`

###### 例题
```php
<?php
$flag = "flag{test}";
$temp = "1337a";
is_numeric($temp)?die("nope"):NULL;    
if($temp>1336){
    echo $flag;
} 
?>
```

* 代码中先将变量放到`is_numeric`函数中判断，如果数字或数字字符串则返回true，否咋返回false。然后一个判断，如果temp大于1336则显示flag。这里用到了PHP弱类型的一个特性，**当一个整型和一个其他类型行比较的时候，会先把其他类型`intval`再比**。如果输入一个`1337a`这样的字符串，在is_numeric中返回true，然后在比较时被转换成数字1337，这样就绕过判断输出flag。

#### bool欺骗
> 当存在`json_decode`和`unserialize`的时候，部分结构会被解释成`bool类型`，也会造成欺骗。

##### `json_decode`
```php
$json_str = '{"user":true,"pass":true}';
$data = json_decode($json_str,true);
if ($data['user'] == 'admin' && $data['pass']=='secirity')
{
    print_r('logined in as bool'."\n");
}
```

运行结果：

```
root@kali:/var/www# php /root/php/hash.php
logined in as bool
```

##### `unserialize`
```php
$unserialize_str = 'a:2:{s:4:"user";b:1;s:4:"pass";b:1;}';
$data_unserialize = unserialize($unserialize_str);
if ($data_unserialize['user'] == 'admin' && $data_unserialize['pass']=='secirity')
{
    print_r('logined in unserialize'."\n");
}
```

运行结果如下：

```
root@kali:/var/www# php /root/php/hash.php
logined in unserialize
```

**bool类型的true跟任意字符串可以弱类型相等**。因此我们可以构造bool类型的序列化数据 ，无论比较的值是什么，结果都为true。（`a`代表`array`，`s`代表`string`，`b`代表`bool`，而`数字`代表个数/长度）

#### 数字转换欺骗
```php
$user_id = ($_POST['user_id']);
if ($user_id == "1")
{
    $user_id = (int)($user_id);
    #$user_id = intval($user_id);
    $qry = "SELECT * FROM `users` WHERE user_id='$user_id';";
}
$result = mysql_query($qry) or die('<pre>' . mysql_error() . '</pre>' );
print_r(mysql_fetch_row($result));
```

将`user_id=0.999999999999999999999`发送出去得到结果如下：

```
Array
(
    [0] => 0
    [1] => lxx'
    [2] => 
    [3] => 
    [4] => 
    [5] => 
)
```

本来是要查询user_id的数据，结果却是`user_id=0`的数据。**`int`和`intval`在转换数字的时候都是`就低`的**，再如下代码:

```php
if ($_POST['uid'] != 1) {
 $res = $db->query("SELECT * FROM user WHERE uid=%d", (int)$_POST['uid']);
 mail(...);
} else {
 die("Cannot reset password of admin");
}
```

假如传入`1.1`，就绕过了`$_POST['uid']！=1`的判断，就能对`uid=1`的用户进行操作了。另外`intval`还有个**尽力模式**，就是**转换所有数字直到遇到非数字为止**，如果采用:

```php
if (intval($qq) === '123456')
{
    $db->query("select * from user where qq = $qq")
}
```

攻击者传入`123456 union select version()`进行攻击。

### 内置函数的参数的松散性
`内置函数的松散性`说的是，**调用函数时给函数传递函数无法接受的参数类型**。解释起来有点拗口，还是直接通过实际的例子来说明问题，下面会重点介绍几个这种函数。

#### md5()
```php
$array1[] = array(
    "foo" => "bar",
    "bar" => "foo",
);
$array2 = array("foo", "bar", "hello", "world");
var_dump(md5($array1)==var_dump($array2));	//true
```

PHP手册中的`md5()`函数的描述是`string md5 ( string $str [, bool $raw_output = false ] )`，`md5()`中的需要是一个`string`类型的参数。但是当你传递一个`array`时，`md5()`不会报错，只是会无法正确地求出array的md5值，md5的结果都是`null`这样就**会导致任意2个array的md5值都会相等**。

##### 例题
注意以下代码,需要判断username和password的md5运算相等才会显示flag

```php
<?php
error_reporting(0);
$flag = 'flag{test}';
if (isset($_GET['username']) and isset($_GET['password'])) {
    if ($_GET['username'] == $_GET['password'])
        print 'Your password can not be your username.';
    else if (md5($_GET['username']) === md5($_GET['password']))
        die('Flag: '.$flag);
    else
        print 'Invalid password';
}
?>
```
这时候给`username`和`passwor`d传入`数组`,即可拿到flag
```
http://www.example.com/index.php?username[]=1&password[]=2
```

#### strcmp()
`strcmp()`函数在PHP官方手册中的描述是`int strcmp ( string $str1 , string $str2 )`,需要给`strcmp()`传递2个string类型的参数。如果str1小于str2,返回-1，相等返回0，否则返回1。strcmp函数比较字符串的`本质`是**将两个变量转换为ascii，然后进行减法运算，然后根据运算结果来决定返回值**。
如果传入给出`strcmp()`的参数是`数组`呢？

```php
$array=[1,2,3];
var_dump(strcmp($array,'123')); //结果是null
```

在某种意义上`null`也就是相当于`false`

##### 例题
```php
<?php 
if (isset($_GET['password'])) {  
    if (strcmp($_GET['password'], $flag) == 0)  
        die('Flag: '.$flag);  
    else  
        print 'Invalid password';  
}
?>
```
使用`strcmp`去比较password和flag，如果`==0`的话，就给出flag，但是`strcmp`比较，**只有相等才会返回0，如果不相等的 话，要么大于0，要么小于0**，但是strcmp只会处理字符串参数，如果**给个数组的话呢，就会返回NULL,而判断使用的是`==`，`NULL==0`是 `bool(true)`的**

#### switch()
* **如果switch是数字类型的case的判断时，switch会将其中的参数转换为int类型**。如下：

```php
$i ="2abc";
switch ($i) {
case 0:
case 1:
case 2:
    echo "i is less than 3 but not negative";
    break;
case 3:
    echo "i is 3";
}
```
这个时候程序输出的是`i is less than 3 but not negative`，是由于`switch()`函数将`$i`进行了类型转换，转换结果为`2`。

#### in_array()
在PHP手册中，`in_array()`函数的解释是`bool in_array ( mixed $needle , array $haystack [, bool $strict = FALSE ] )`,如果`strict`参数没有提供，那么in_array就会使用松散比较来判断`$needle`是否在`$haystack`中。当strince的值为true时，`in_array()`会比较`needle`的类型和`haystack`中的**类型是否相同**。

```
in_array — 检查数组中是否存在某个值 参数
needle 待搜索的值。
注意: 如果 needle 是字符串，则比较是区分大小写的。
haystack 这个数组。
strict 如果第三个参数 strict 的值为 TRUE 则 in_array() 函数还会检查 needle 的类型是否和 haystack 中的相同。
可以看到，只有加了strict才会对类型进行严格比较
```

```php
$array=[0,1,2,'3'];
var_dump(in_array('abc', $array));  //true
var_dump(in_array('1bc', $array));	//true
// 它遍历了array的每个值，并且作"=="比较（“当设置了strict 用===”）
```

可以看到上面的情况返回的都是true,**因为’abc’会转换为0(`intval('abc')=0`)，’1bc’转换为1(`intval('1bc')=1`)**。
`array_search()`与`in_array()`也是一样的问题。

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/_1527742998_24616_1536892885)


