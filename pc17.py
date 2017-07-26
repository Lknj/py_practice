# coding:utf-8

from sys import argv

from os.path import exists

script, from_file, to_file = argv
print("Copying from %s to %s" %(from_file, to_file))

# we could do these two on one Line too,how?
# 打开文件
input = open(from_file)
# 读文件
indata = input.read()
print("The input file is %d byte long" %len(indata))#len（）字符串长度

# exists 这个命令将文件名字作为参数，如果文件存在，返回True，否则返回False。
print("Does the output file exist? %r" %exists(to_file))
print("readly,hit RETURN to continue, CTRL-C to abort.")

#打开文件，写模式
output = open(to_file,'w')
#写入要拷贝的内容
output.write(indata)
print("Alright, all done.")
#关闭文件，保存
output.close()
input.close()
