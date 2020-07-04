import sys

name = 'Gusest'

if len(sys.argv)>1:
    name = sys.argv[1]
print('hello,{}'.format(name))
