# 搭建Git服务器
 1、安装git apt install git
 2、创建用户 useradd git
 3、创建登陆证书
    收集所有需要登陆的用户的公钥，id_rsa.pub 
    把所有公钥导入到/home/git/.ssh/authorized_keys文件里，一行一个
 4、初始化git仓库
 先选定一个目录作为git仓库，例如/srv/simple.git,在srv目录下输入命令：

sudo git init  --bare simple.git

git会创建一个裸仓库，裸仓库没有工作区。把Owner 改为 git.

chown -R git:git simple.git

5 、禁用shell登陆

修改/etc/passwd 文件

git:x:1001:1001:,,,:/home/git:/bin/bash

修改为：

git:x:1001:1001:,,,:/home/git:/usr/bin/git-shell

 6、克隆远程仓库

git clone git@server:/srv/simple.git


