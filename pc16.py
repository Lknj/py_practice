# coding:utf-8

from sys import argv

script, filename = argv

print("We're going to erase %r." %filename)
print("If you don't want that,hit CTRL-c (^C).")
print("If you do want that,hit RETURN.")

input("?")
print("Opening the file...")
#打开你所输入的文件，写模式
target = open(filename,'w')

print("Truncating the file.  Goodbay!")
#清空文件
target.truncate()

print("Now I'm going to ask you for three lines.")
#写
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
#写入文件
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
target.write(line1 + "\n"+line2 + '\n' + line3 + "\n")

print("And finally, we close it.")
#关闭文件（保存）
target.close()
