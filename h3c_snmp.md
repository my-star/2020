#  SNMP 简介

#### 1.1.1 SNMP的网络架构
 SNMP的网络架构由三部分组成：NMS、Agent、MIB
- NMS(Network Management System,网络管理系统）是SNMP网络的管理者，能够提供友好的人机交互界面，方便网络管理员完成大多数的网络管理工作。
- Agent是SNMP网络的被管理者，负责接收、处理来自NMS的SNMP报文。在某些情况下，如接口状态发生改变时，Agent也会主动向NMS发送警告信息
- MIB(Management information Base ,管理信息库）是被管理对象的集合。NMS管理设备的时候，通常会关注一些设备的参数，比如接口状态，cpu利用率等，这些参数就是被管理对象，在MIB中成为节点。每个Agent都有自己的MIB.MIB定义了节点之间的层次关系以及对象的一些列属性，比如对象的名称、访问权限、和数据类型等。被管理设备都有自己的MIB文件，在NMS上编译这些MIB文件，就能生成该设备的MIB.NMS根据访问权限对MIB节点进行读/写操作，从而实现对Agent的管理。
#### 1.1.2 MIB和MIB视图

