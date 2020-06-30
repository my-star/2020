# Ubuntu 设置代理
---

原文链接：https://blog.csdn.net/kan2016/article/details/90411137

#### 1、配置系统代理
#### 2、配置apt代理
```
	sudo vim /etc/apt/apt.conf

	Acquire::http::Proxy "http://192.168.100.101:8080/";
```
#### 3、配置好apt之后，就可以终端联网更新

```
	sudo apt update

	sudo apt upgrade

```
```
	sudo rm /var/lib/apt/lists/lock
```
#### 4、配置curl ,wget,pip 代理

打开 bashrc 文件
```
	sudo vim ~/.bashrc

```
```
	export http_proxy='http://proxy.xxx.com:8080'
	export https_proxy='http://proxy.xxx.com:8080'
	export ftp_proxy='http://proxy.xxx.com:8080'
	export no_proxy='localhost,127.0.0.1'
```
执行：
```
	source ~/.bashrc
```
#### 5、git proxy

```
	#设置代理
	git config --global http.proxy http://proxy.xxx.com:8080
	#查看代理
	git config --global http.proxy
	#删除代理
	git config --global --unset http.proxy
	git config --global --unset https.proxy
```

#### 6、Docker proxy
- （1）添加用户到docker 组
```
	sudo groupadd docker
	
	sudo gpasswd -a admin docker

	cat /etc/group
```
注意:如果提示get ......dial unix /var/run/docker.sock权限不够
则修改/var/run/docker.sock权限
```
	sudo chmod a+rw /var/run/docker.sock
```
- (2)使用本地源
```
curl -sSL https://get.daocloud.io/daotools/set_mirror.sh | sh -s http://f1361db2.m.daocloud.io

```
- (3)配置代理，需要ROOT权限
```
	sudo su

	mkdir  -p /etc/systemd/system/docker.service.d

	touch /etc/systemd/system/docker.service.d/http-proxy.conf

	chmod 775 http-proxy.conf

	vim http-proxy.conf
```
修改后的内容：
```
	[Service]
	Environment ="HTTP_PROXY=http://proxy.xxx.com:8888" "NO_PROXY=localhost,127.0.0.1"
```
刷新配置
``` 
	systemctl daemon-reload
```
重启服务
```
	system restart docker
```
查看配置
```
	systemctl show --property=Environment docker
```
OK!

