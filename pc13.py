# coding:utf-8

#import调用
from sys import argv
#解包,把argv（参数变量）里的所有参数依次赋予左边的变量名
script,first,second,third = argv

print("The script is called:", script)
print("Your firstvariable is:", first)
print("Your second variable is:", second)
print("Your third varible is:",third)
