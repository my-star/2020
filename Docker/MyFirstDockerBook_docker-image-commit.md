# MyFirstDockerBook
---
## 使用Docker commit 提交镜像
##### 查找镜像
```
# docker search mysql
```
##### 拉取镜像
```
# docker pull mysql
```
##### 使用镜像创建容器
```
# docker run -i -t mysql  /bin/bash

```
我们以交互的方式启动了该容器，并且在里面运行了Bash shell.

#### 构建镜像
- 使用Docker commit 命令
- 使用Docker build 命令和Dockerfile文件

> 一般来说，我们不是真正“创建”新镜像，而是基于一个已有的基础镜像，如ubuntu或fedora等，构建新镜像。
> 从零开始构建全新的镜像，请参考https://docs.docker.com/articles/baseimages/

1、创建Docker Hub 账号 
https://hub.docker.com/account/signup/

登录到DockerHub

```
# docker login
Username:
Password:
Email:
LoginSucceeded
```
> 个人认证信息会保存到$HOME/.dockercfg文件中

2、使用Docker的Commit命令创建镜像

首先创建一个容器，并在容器里做出修改，最后再将修改提交为一个新镜像。

1）创建一个要进行修改的定制的容器
```bash
$ sudo docker run -i -t ubuntu /bin/bash

root@4aab3e3cb76 :#
```
2）接下来，在容器中安装Apache
```bash
root@4aab3e3cb76 :# apt-get -yqq  update

.....

root@4aab3e3cb76 :# apt-get -y install apache2

```
我们启动了一个容器，并在里面安装了Apache 。我们会将这个容器作为一个Web服务器来运行，所以我们想把它的当前状态保存下来。这样就不必每次创建一个新容器并再次安装Apache.使用exit命令从容器中退出，之后在运行docker commit 命令。


```
docker commit 5613983f380e gblacker/apache2


sha256:5b49771596e99da655628a29374dc199ea3f0c10f3e6042d1fb551454caaac75

```
> 需要注意的是，docker commit 提交的只是创建容器的镜像与容器当前状态之间由差异的部分，这使得该更新非常轻量


查看新创建的镜像

```
$ docker images gblack/apache2
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu              latest              74435f89ab78        2 weeks ago         73.9MB
```
提交另一个新的定制容器

```
docker commit -m ='A new custom image' --author='star' 5613983f380e gblacker/apache2:webserver

sha256:c56c63a59264b34a17061c644f312f81b3e7ded63dc9e5f7d37fa6f68edca63e
```
查看提交的镜像的详细信息

```
$ docker inspect gblacker/apache2:webserver

{
        "Id": "sha256:c56c63a59264b34a17061c644f312f81b3e7ded63dc9e5f7d37fa6f68edca63e",
        "RepoTags": [
            "gblacker/apache2:webserver"
        ],
        "RepoDigests": [],
        "Parent": "sha256:74435f89ab7825e19cf8c92c7b5c5ebd73ae2d0a2be16f49b3fb81c9062ab303",
        "Comment": "=A new custom image",
        "Created": "2020-07-02T15:00:12.889497901Z",
        "Container": "5613983f380ed348de9bb2b64a66f26da825330f93ec8b42f27a6876dd83ec6e",
        "ContainerConfig": {
            "Hostname": "5613983f380e",
            "Domainname": "",
            "User": "",
            "AttachStdin": true,
            "AttachStdout": true,
            "AttachStderr": true,
            "Tty": true,
            "OpenStdin": true,
            "StdinOnce": true,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/bash"
            ],
            "Image": "ubuntu",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {}
        },
        "DockerVersion": "19.03.6",
        "Author": "star",
        "Config": {
            "Hostname": "5613983f380e",
            "Domainname": "",
            "User": "",
            "AttachStdin": true,
            "AttachStdout": true,
            "AttachStderr": true,
            "Tty": true,
            "OpenStdin": true,
            "StdinOnce": true,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
```
使用刚构建的新镜像运行一个容器，使用docker run 命令

```
 $ sudo docker run -i -t gblacker/apache2:webserver
```
