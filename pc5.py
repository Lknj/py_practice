# -*- coding:utf-8 -*-
name = 'Zed A.Shaw'
age = 35 # not a lie谎言
height = 74 # inches 英寸
weight = 180 # lbs 磅
eyes = 'Blue'
teeth = 'white'
hair = 'Brown'
my_height = height * 2.54
my_weight = weight * 0.4535924
print("Let's talk about %s." %name)
print("He's %d inches tall." %height)
print("He's %d pounds heavy." %weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." %(eyes,hair))
print("His teeth  are usually %s depending on the coffee."%teeth)

# this line is tricky, try to get it exactly right
# 这行很复杂，试着把他弄清楚

print("If I add %d,%d,and %d I get %d." %(age,height,weight,age + height + weight))

print("I am %d inches tall." %my_height)
print("I am %d pounds heavy." %my_weight)
