# coding:utf-8

i = 0

numbers = []


while i < 6:
    print("at the top i is %d" % i)
    numbers.append(i) # 列表的append函数，添加
    i = i + 1
    print("Number now:",numbers)
    print("At the bottom i is %d" % i)

print("---------------------------")
print("the numbers:")


for num in numbers:
    print(num)
    
