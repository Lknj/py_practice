# coding:utf-8

# 定义函数
def add(a, b):
    print("ADDING %d + %d" %(a, b))
    return a + b #返回a+b的结果，将a+b的值赋予一个变量

def subtract(a, b):
    print("SUBTRSCTING %d - %d" %(a, b))
    return a - b

def multiply(a, b):
    print("MULTIPLYING %d * %d" %(a, b))
    return a * b

def divide(a, b):
    print("DIVIDING %d / %d" %(a, b))
    return a / b


print("Let's do some math with just functions!")

# 赋予变量函数返回的值
age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq))

# A puzzle for the extra credit, type it in anyway.
# 额外学分的一个难题，无论如何否要解决他

print("Here is a puzzle.")

# 函数乱斗，md，不会解释，反正函数赋予变量值，从最里面的函数一个一个算
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That become: ", what, "Can you do it by hand?")
