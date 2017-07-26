# coding:utf-8
#调用
from sys import argv
#给参数赋予变量名
script, filename = argv
#接受一个参数，返回一个值，将这个值赋予变量，打开文件的过程
txt = open(filename)

print("Here's your file %r:" %filename)

#执行read命令
print(txt.read())

print("Type the filename again:")

file_again = input(">")

txt_again = open(file_again)
#打开你所输入的文件
print(txt_again.read())
print(txt.close())
