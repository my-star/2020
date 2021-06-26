# 构建SSH功能的Ubuntu镜像 

> 参考链接：https://www.jianshu.com/p/a97faf8b6da1
> 参考链接：https://www.cnblogs.com/guoxiangyue/p/10021885.html

### 1、创建工作目录

目录的文件结构：
Dockerfile  	构建Docker镜像必备
run.sh      	容器启动时需要运行的命令
authorized_keys rsa密钥，由本机生成
### 2、编写启动脚本和生成密钥
run.sh
```bash
#! /bin/bash

/usr/sbin/sshd -D
```
在宿主机上生成SSH密钥对，并创建authorized.keys
```bash
$ ssh-keygen -t rsa 
```
### 3、创建Dockerfile 文件

```
FROM ubuntu
MAINTAINER "UBUNTU SSH IMAGES"
# apt-get 换源
RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
RUN apt-get update

#安装ssh服务
RUN apt-get install -y openssh-server
RUN mkdir -p /var/run/sshd
RUN mkdir -p /root/.ssh
#安装Telnet服务

RUN apt-get install -y telnet

#配置SSH
#设置ssh远程登陆密码
RUN echo "root:123456" | chpasswd
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  

#复制Rsa文件到相应位置，并赋予脚本可执行权限

ADD authorized_keys /root/.ssh/authorized.keys
ADD run.sh /run.sh
RUN chmod 755 /run.sh

#开放端口

EXPOSE 22

#设置自启动命令
CMD ["/bin/bash","run.sh"]
