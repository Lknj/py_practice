# coding:utf-8

# this one is like your script  with argv
# 这是一个你喜欢的脚本的参数

# 创建一个函数，def后是函数名字，
# *argv跟脚本的argv非常相似，参数必须放在括号里才能正常工作
def print_two(*args):
    arg1, arg2 = args

    print("arg1: %r, arg2: %r" %(arg1, arg2))

# ok, that *args is actually pointless,we can just do this
# *args 其实是毫无意义的，我们可以这样做

# 创建函数，将（）里的作为变量名，可以跳过整个解包的过程
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" %(arg1, arg2))

# this just takes one argument
# 这只需要一个参数

def print_one(arg1):
    print("arg1: %r" %arg1)

# this one takes no arguments
# 这个不需要参数

def print_none():
    print("I got nothing'.")


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
