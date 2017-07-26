# coding:utf-8

# 调用方法
from sys import argv
# 将所有的参数放在argv（同一个变量）下，赋予每个参数变量名
# 将argv里的东西解包，将所有参数 依次赋予左边的变量名
script, user_name = argv
prompt = '>'

print("Hi %s,I'm the %s script." %(user_name,script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" %user_name)

likes = input(prompt)

print("Where do you live %s?" %user_name)

lives = input(prompt)

print("What kind of computer do you have?")

computer = input(prompt)

print("""
Alright,so you said %r about liking me.
You live in %r,Not sure where that is.
And you have a %r computer. Nice.
""" %(likes,lives,computer))
