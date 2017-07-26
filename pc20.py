# coding:utf-8

from sys import argv

script, input_file = argv

# 定义函数
def print_all(f):
    print(f.read())

# file.seek()移动文件读取指针到指定位置
def rewind(f):
    f.seek(0)

# 定义函数，读取文件的一行file.readline()
def print_a_line(line_count,f):
    print(line_count, f.readline())

# 打开文件
current_file = open(input_file)

print("First let's print the whole file:\n")

# 读文件
print_all(current_file)

print("Now let's rewind,kind of like a tape.")

# 把文件的读取指针移到开头（从头开始读取）
rewind(current_file)

print("Let's print three lines:")

# 给变量赋值
current_line = 1
# 调用函数，读取文件的一行
print_a_line(current_line, current_file)

# 变量的值+1，从当前位置，也就是读取一行后的位置开始，接着读取文件的一行
current_line = current_line + 1
print_a_line(current_line, current_file)

# 同上
current_line = current_line + 1
print_a_line(current_line, current_file)

# 关闭文件
current_file.close()
