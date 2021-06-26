#  Zabbix In  Docker 

### docker images download
zabbix 在容器中安装由两种方法：

#### 1、分体式镜像通过相互链接工作
每个镜像相对来收比较小，拷贝相当方便
其中包括：mysql-server,zabbix-server-mysql,zabbix-web-apache,javagate
在此先列举一些情况吧。

通过示例命令无法正常启动Docker,现在找到官方的安装命令

#### 示例：运行MySQL 数据库支持、基于Nginx Web 服务器的Zabbix Web 界面和 Zabbix Java gateway

- 1、首先启动空的MySQL服务器实例。

1、Start empty MySQL server instance

```bash
# docker run --name mysql-server -t \
	-e MYSQL_DATABASE="zabbix" \
	-e MYSQL_USER="zabbix" \
	-e MYSQL_PASSWORD="zabbix_pwd" \
	-e MYSQL_ROOT_PASSWORD = "root_pwd" \
	-d mysql:5.7 \
	--character-set-server=utf8 --collation-server=utf8_bin
```
- 2、其次，启动Zabbix Java gateway实例

2、Start Zabbix Java gateway instance
```bash
# docker run --name zabbix-java-gateway -t \
	-d zabbix/zabbix-java-gateway:latest
```
- 3 、然后，启动Zabbix server实例，并将其关联到已创建的MySQL server 实例

3、Start Zabbix server instance and link the instance with created MySQL server instance
```bash
# docker run --name zabbix-server-mysql -t \
	-e DB-SERVER_HOST="mysql-server" \
	-e MYSQL_DATABASE="zabbix" \
	-e MYSQL_USER = "zabbix" \
	-e MYSQL_PASSWORD="zabbix_pwd" \
	-e MYSQL_ROOT_PASSWORD="root_pwd" \
	-e ZBX_JAVAGATEWAY="zabbix-java-gateway" \
	--link mysql-server:mysql \
	--link zabbix-java-gateway:zabbix-java-gateway \
	-p 10051:10051 \
	-d zabbix/zabbix-server-mysql:latest
```
- 4、最后，启动Zabbix Web界面，并将其关联到已创建的MySQL server 和 Zabbix server实例。

4、Start Zabbix web interface and link the instance with created MySQL server and Zabbix server instance
```bash
# docker run --name zabbix-web-nginx-mysql -t \
	-e DB_SERVER_HOST="mysql-server" \
	-e MYSQL_DATABASE="zabbix" \
	-e MYSQL_USER="zabbix" \
	-e MYSQL_PASSWORD="zabbix_pwd" \
	-e MYSQL_ROOT_PASSWORD="root_pwd" \
	--link mysql-server:mysql \
	--link zabbix-server-mysql:zabbix-server \
	-p 80:80 \
	-d zabbix/zabbix-web-nginx-mysql:latest
```
####2、集合式镜像 zabbix-appliance 整合各种组件到一个镜像之中

此镜像使用方便，只需要一个命令即可开启。

