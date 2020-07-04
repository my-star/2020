判断语句if

导入系统API

import sys

定义初始变量

name =‘Guest’   //单引号和双引号都可以使用，成对出现就可以

判断输入是否有输入参数sys.argv[]

if len(sys.argv)>1:
	name = sys.argv[1]
如果有参数输入则把参数赋值到name变量中

格式化输出变量 format

print ('hello,{}'.format(name))
