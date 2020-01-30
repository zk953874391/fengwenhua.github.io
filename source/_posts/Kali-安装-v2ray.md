---
title: Kali 安装 v2ray
date: 2020-01-26 18:47:20
tags:
- v2ray
- proxychains4
categories:
- Linux
- Kali
---
## 安装

```bash
bash <(curl -L -s https://install.direct/go.sh)
```

## 开机自启
```
gedit /etc/systemd/system/v2ray.service
```

<!--more-->
在里面填写如下内容：

```service
[Unit]
Description=V2Ray Service
After=network.target
Wants=network.target

[Service]
# This service runs as root. You may consider to run it as another user for security concerns.
# By uncommenting the following two lines, this service will run as user v2ray/v2ray.
# More discussion at https://github.com/v2ray/v2ray-core/issues/1011
# User=v2ray
# Group=v2ray
Type=simple
PIDFile=/run/v2ray.pid
ExecStart=/usr/bin/v2ray/v2ray -config /etc/v2ray/config.json
Restart=on-failure
# Don't restart in the case of configuration error
RestartPreventExitStatus=23

[Install]
WantedBy=multi-user.target
```

配置生效：

```bash
systemctl enable /etc/systemd/system/v2ray.service
```

## 配置 ProxyChain

ProxyChain 不用安装，它是 Kali 自带的一个工具，作用在于可以配置任何一个应用的代理。配置文件在 `/etc/proxychains.conf`

```bash
gedit /etc/proxychains.conf
```

取消注释`dynamic_chain`,去掉`#`即可, 然后在文件最后一行把 `socks4 127.0.0.1 9050` 注释掉，换成自己的配置，对应上文这里是 `socks5 127.0.0.1 1081`.

```conf
dynamic_chain

#socks4     127.0.0.1 9050
socks5 127.0.0.1 1081
```

## 测试服务器

测试需要使用 `proxyresolv` 命令，翻译过来就是代理解析器，用来解析目标地址是否连通。格式例如：`proxyresolv www.google.com`，第一次使用时会提示命令未找到，需要将其复制到 `/usr/bin` 下，命令如下：

```bash
cp /usr/lib/proxychains3/proxyresolv /usr/bin/
```

然后再执行 proxyresolv [www.google.com](http://www.google.com) 命令当返回 ok 时则证明配置没问题，如下图：

![](https://gitee.com/fengwenhua/ImageBed/raw/master/1580037275_20200126190943963_475169139.png)

## ProxyChains 代理

以上配置好后，就可以通过 ProxyChains 来代理任何一个应用，格式为：`proxychains 应用名称`，例如 `proxychains firefox，proxychains sqlmap，proxychains msfconsole` 等。

![](https://gitee.com/fengwenhua/ImageBed/raw/master/1580037276_20200126191205507_1823519627.png)


