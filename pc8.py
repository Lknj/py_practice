# -*- coding:utf-8 -*-

# 变量的值含有格式化字符
formatter = "%r%r%r%r"
# 嵌用格式化
print(formatter %(1,2,3,4))
print(formatter %("one","two","three","four"))
print(formatter %(True,False,True,False))
print(formatter %(formatter,formatter,formatter,formatter))

print(formatter %(
    "I had this thing.",
    "That you could type up right",
    "But it didn't sing.",
    "So I said goodnight."
    ))
