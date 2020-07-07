### 0.2执行命令
bash 的核心功能是执行系统命令。在bash shell 中 echo 命令可以在屏幕上显示文本
```
$ echo "hello world"
```
输入当前环境变量
```
$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games

```
输出中的各个目录之间以分号分隔。当需要运行程序或命令时，bash会检查所有这些目录。如果命令没有在其中，bash就无法执行，另外需要注意的时，bash是以这些目录在PATH中出现的顺序依次检查的。顺序在这里很重要。如果两个同名命令分别位于PATH中两个不同的目录中，可能会由于目录出现的先后顺序产生不同的结果。
可以用which 命令查看命令在PATH中的位置。

```
$ which python
/usr/bin/python
```
知道了这些信息就可以把需要测试的文件移动或复制到PATH目录中，然后就可以执行命令
> which 命令可以确定PATH命令的完整路径。
### 0.3 配置登录脚本

可以配置PATH环境变量，使得在启动新的Shell时，可以向其他命令那样自动调用定制脚本。

新命令shell启动后的第一件事是读取用户主目录(/home/<username>)中的登录脚本并执行其中的定制命令。根据你所用的系统，登录脚本可以是.login、.profile、.bashrc、.bash_profile.要想知道具体是哪个，像下面这样在这些文件中加入一行：
```
echo this is .profile
```
这些内容会出现在登录窗口顶端，可以看到登录时载入的是哪个登录脚本。

> 将工作目录添加到PATH

```
$ cat ~/.bashrc

export PATH="/path/to/scripts/$PATH"

```
开发脚本中的任何命令都可以向其他命令一样执行
### 0.4 运行Shell 脚本


