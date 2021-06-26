# Local Docker repository

## 搭建Docker 私有仓库
Docker 默认命令使用Docker Hub.

如何在本地创建私有仓库服务器：
Docker 仓库服务器名为Docker 注册(registry)服务器。
docker push 将镜像上传到服务器
docker pull 下载镜像

Docker 注册服务器有多种存储镜像的方法：

- 1、存储镜像数据到本地

> Docker 注册服务器也是Docker Hub 提供的Docker 镜像。
首先下载Docker 注册镜像。
```
$ sudo docker pull registry:latest
```
以容器运行registry:latest 镜像
```
$ docker run -d --name= hello-registry \
	-p 5000:5000 \
	-v /tmp/registry:/tmp/registry \
	registry
```
运行后，镜像文件存储到主机的 /tmp/registry 目录

	注册服务器
——————————————————————————————————————————

Docker注册容器<----------->/temp/registry

__________________________________________
docker push/pull

服务器| Docker 镜像

将镜像数据存储到Docker注册和本地

- 2、上传镜像
向私有仓库上传镜像时，需要先创建标签。使用Docker tag命令为镜像创建标签。
```
$ sudo docker tag hello:0.1 localhost:5000/helloL:01
$ sudo docker push localhost:5000/hello:0.1
```
