#!/usr/bin/python3 
# -*- coding:utf-8 -*-
#第一行指出可用python3去执行它，没什么用

#赋值,说明一下，下划线_ 在变量里用作假想的空格
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

# 计算
cars_not_driven = cars - drivers

cars_driven = drivers

carpool_capacity = cars_driven * space_in_a_car

average_passengers_per_car = passengers / cars_driven

# 输出
print("There are",cars,"cars available.")
print("There are only",drivers,"drivers available.")
print("There will be",cars_not_driven,"empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print("We have",passengers,"to carpool today.")
print("We need to put about",average_passengers_per_car,"in each car.")

