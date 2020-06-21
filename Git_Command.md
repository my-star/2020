# Git 学习指南
## 0X1基本概念
---
## 基本概念 :books:
> 介绍一个分布版本控制系统的设计思路，以及它与集中式版本控制系统的不同之处。
> 了解分布式版本库的具体工作方式。
### 1.1  分布式版本控制，有何过人之处


  _集中式版本控制_



_分布式版本控制_

## 0X2 入门 :football:
### 2.1准备Git环境
- [Git 官网](http:\\git-scm.com\download)
##### 配置用户名和用户邮箱
`> git config --global user.email "hans@mustermann.de"`
### 2.2  第一个Git项目
- :open_file_folder: Projects
  -  :open_file_folder: first_step
        - :newspaper: bar.txt
        - :newspaper: foo.txt

##### 2.2.1 创建版本库
  首先创建一个版本库，用于存储该项目本身及历史版本。
  需要在该项目中使用 `init` 命令。
  对于一个带版本库的项目目录，我们通常称之为工作区。
  ```shell
    > cd \projects\first_step
    > git init
    Initialized empty Git repository in \home\pi\projects\first_step\.git\
  ```
`init` 命令会在上述目录中创建一个名为.git 的隐藏目录，并在其中创建一个版本库。

##### 2.2.2 首次提交

将文件添加到版本库中。通常将项目的一个版本称为一次提交
- 1、使用 `add` 命令来确定那些文件应被包含在提交中
- 2、利用 `commit` 命令将修改传送到版本库中，并赋予该提交一个散列值以表示这次新提交。
```bash
> git add foo.txt bar.txt
> git commit --message "Sample project imported"
[master (root-commit) 96da62b] Sample project imported
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 bar.txt
 create mode 100644 foo.txt
```
##### 2.3 检查状态
```bash
> rm bar.txt
> touch bar.html
>
> git status
 On branch master
 Changes not staged for commit:
  (use "git add\rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        deleted:    bar.txt

 Untracked files:
  (use "git add <file>..." to include in what will be committed)

        bar.html

no changes added to commit (use "git add" and\or "git commit -a")
```
使用`diff` 命令比较文件之间的不同

```bash
> git diff foo.txt
 diff --git a\foo.txt b\foo.txt
 index e69de29..4c8016d 100644
 --- a\foo.txt
 +++ b\foo.txt
 @@ -0,0 +1,6 @@
 +<html>
 +<head>
 +        <title>
 +<\head>
 +<body>
 +<\body>
```
>可以详细记录每一行数据的操作
##### 2.2.4  提交修改
```bash
 > git add foo.txt bar.html
 > git rm bar.txt
 rm 'bar.txt'
```
```bash
> git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        renamed:    bar.txt -> bar.html
        modified:   foo.txt
```
然后用 `commit` 命令提交这些修改
```shell
> git commit --message "SomeChanges"
 2 files changed, 6 insertions(+)
 rename bar.txt => bar.html (100%)
```
##### 2.2.5显示历史
```bash
> git log
commit e5835239bf39be531fb1ee5070a111a399fdc014 (HEAD -> master)
Author: my-star <1281601990@qq.com>
Date:   Sat Jun 20 17:41:24 2020 +0000

    SomeChanges

commit 96da62bde1e4c05376a5eb47b266b93290ba4801
Author: my-star <1281601990@qq.com>
Date:   Sat Jun 20 17:23:08 2020 +0000

    Sample project imported
```
