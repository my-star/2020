## Install squid(http_proxy) on CentOS 8

2020-06-24

#### 1、cat  version of the system.
```bash
	$ cat /etc/redhat-release
```
#### 2、cat the software version in response  && install 
```bash
	$ yum list |grep squid
```
```bash
	$ sudo yum install -y squid
```
#### 3、config squid 
```bash
	$whereis squid

	$ sudo vim /etc/squid/squid.conf

```
	something wrong you maybe get:
	
	acl localnet / http_access localnet

	need add `acl localhost 1.1.1.1` and `http_access localhost 1.1.1.1`

	localnet/localhost is a group,default rules `deny any` 

	set http_proxy_port against the default port will safer! :star:


#### 4、check config file
```bash
	$ squid -k parse
```

#### 5、config firewall 

	open port you set at third step

```
	$ sudo firewall-cmd --add-port = 8888/tcp --zone=public --permenent(forever)

	# firewall-cmd --remove-port=8888/tcp --zone=public --permenent	

	#reload the rule of firewall

	firewall-cmd --reload
```


#### 6、restart service

```bash
	$ service squid start

	$service enable squid  now

	$service start squid
```
	if something wrong at config file ,the service will start not success!

#### 7、test proxy
localhost:	
```bash
	$ curl -x 127.0.0.1:8888 baidu.com
```
proxy client:
```bash
	$ curl -x 10.1.1.8:8888 baidu.com
```
