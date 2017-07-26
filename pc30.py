# coding:utf-8

# this first kind of for-loop goes through a list

the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

# 第一种for循环通过列表

for number in the_count:
    print("This is count %d" % number)


# same as above 同上

for fruit in fruits:
    print("A fruit of type: %s" % fruit)


# also we can go through mixed lists too
# 我们也可以通过混合列表
# notice we have to use %r since we don't know what's in it
# 注意 我们必须用%r 因为我们不知道里面有什么

for i in change:
    print("I got %r" %i)

# we can also build lists, first start with anempty one
# 我们也可以创建列表，首先从空列表开始

elements = []

# 使用range函数  做0到5个计数
for i in range(0,6):
    print("Adding %d to the list." % i)

    # append is a function that list understand
    # append是列表理解的函数

    elements.append(i)

# now we can print them out too 输出

for i in elements:
    print("elements was: %d" % i)
    
