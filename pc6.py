x = "There are %d type of people." %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" %(binary,do_not)

print (x)
print (y)

# 用%r打印变量的“原始”数值，%s只是字符串
print("I said: %s." %x) 
print("I also said:'%s'." %y)

hilarious = False

joke_evaluation = "Isn't that joke so funny?!%r"

print(joke_evaluation %hilarious)

w = "This is the left side of ..."
e = "a string with a right side."

print (w + e)
