Linux 分区扩容
 ---
查看分区情况和硬盘情况

```
# df -h 
```
>  df - report file system disk space usage

fdisk -l 建立分区 

> fdisk - manipulate disk partition table 

创建物理卷 pvcreate /dev/sda3 可以先执行 partprobe

>  partprobe - inform the OS of partition table changes

查询物理卷  vgscan 

新增物理卷扩展  vgextend centos /dev/sda3

/dev/mapper/centos-root 增加20G

```
#lvextend -L +20G /dev/mapper/centos-root

```
系统还不认识刚刚添加进来的文件系统，需要对文件系统进行扩容
```
# xfs_growfs /dev/mapper/centos-root

```

对磁盘扩容成功


