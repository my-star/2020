# Puppet
---
## 一、puppet 介绍

### 1、puppet是什么

puppet 是一个IT基础设施自动化管理工具，它能够帮助系统管理员管理基础设施的整个生命周期：供应provisioning、配置configuration、联动orchestration、报告reporting
基于puppet ,可实现自动化重复任务、快速部署关键性应用以及在本地或云端完成主动管理变更和快速扩展架构规模等。

### 2、puppet的工作机制

1）工作模型

puppet 通过声明性、基于模型的方法进行IT自动化管理。
定义：通过puppet的声明性配置语言定义基础设置配置的目标状态
模拟：强制应用改变的之前先进行模拟性应用
强制：自动、强制部署达成目标状态，纠正任何偏离的配置
报告：报告当下状态及目标状态的不同，以及达成目标状态所进行的任何的强制性改变

puppet 三层模型

- Configuration Language
- Transactional Layer
- Resource Abstraction Layer

https://www.cnblogs.com/keerya/p/8040071.html
 
