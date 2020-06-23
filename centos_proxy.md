#  CentOS 8  Setting Proxy(yum,git,pip)
---
### yum

cat the file in /etc/yum.conf

add the next line under the bottom of the file:
```bash
	proxy=http://10.0.0.1:80
```
Finish it,You can run `yum update` try it!

### pip

Install Python packages

```bash
	pip install {packagename} --proxy="http://10.1.1.0:80"
```

### git
```bash
	git config --global http.proxy 'http://192.168.100.200:20'
	git config --global https.proxy 'http://192.168.100.200:20'
```
