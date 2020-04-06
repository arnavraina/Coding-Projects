'''
from platform import system
if system() == 'Windows':
    print("Hello")
    command = 'ipconfig'
elif system() == 'Linux':
    command = 'ífconfig'
else:
    print('Os not Found')
print(command)
'''
import os
#cmd = 'ipconfig'
cmd = 'ipconfig/all'
a=os.system(cmd)
print(a[0:10])

import psutil

addrs = psutil.net_if_addrs()
#print(addrs.keys())