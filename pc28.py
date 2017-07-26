# coding:utf-8
# 变量赋值
people = 30
cars = 40
buses = 15

# if语句，如果为True，输出
if cars > people:
    print("We should take the cars.")

elif cars <people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

# 如果 buses > cars，则输出
if buses > cars:
    print("That's too mny buses.")

elif buses < cars:
    print("Maybe we could take the buses.")
# 否则，输出
else:
    print("We still can't decide.")



if people >buses:
    print("Alright,let's just take the buses.")
else:
    print("fine,let's stay home then.")
