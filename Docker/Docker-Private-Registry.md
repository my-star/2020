# Docker private registry
---
### 0x0 Pull down the Registry image
```
$ docker pull registry
```
### 0x1 Run the local registry
```
$ docker run -d -p 5000:5000 --name localregistry registry
```
Check the status of our container use `docker ps`
### 0x2 Pull down a few images and push to localregistry

Step1: Pull down busybox and alpine Linux Images
```
$docker pull busybox

$docker pull alpine

```
Once the images have been pulled down,verity that they are present in your images list via the docker images command.

> Notice that the format for specifying the image in  a specifc regisry as:

[REGISTRY-HOSTNAME:REGISTRY_PORT]/IMAGENAME

For public Docker Hub,we were not specifying the**[REGISTRY_HOSTNAME:REGITRY_PORT]**option.But for our local registry we need to specify that so that the docker client will look there.

Step 2: Push busybox and alpine Linux Images into the localRegistry
```
$ docker push localhost:5000/alpine:latest
```
### 0x3 Search for images in local Registry 
```
$ docker search [my.registry.host]:[port]/library
```
