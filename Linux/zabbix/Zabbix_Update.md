# zabbix update 3.0->5.0
---
### 1、停止Zabbix server
停止Zabbix server 以确保没有新的数据可以写入数据库
#### 查看zabbix版本
```bash
    #rpm -qa |grep zabbix 
    zabbix-agent-3.0.30-2.el7.x86_64
    zabbix-release-3.0-1.el7.noarch
    zabbix-web-3.0.30-2.el7.noarch
    zabbix-web-mysql-3.0.30-2.el7.noarch
    zabbix-server-mysql-3.0.30-2.el7.x86_64
```
停止服务
```bash
    service zabbix-server stop  
    service httpd stop
```
查看MySQL 数据文件路径
```bash
$ ps -ef |grep mysql
```
usr/lib/mysql:mysql运行路径
var/lib/mysql:mysql数据库文件的存放路径
usr/lib/mysql:mysql的安装路径

