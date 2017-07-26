# coding:utf-8

# 字典
cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FI': 'Jacksonxille'}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
# 定义函数
def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "Not found."

cities['_find'] = find_city

# 循环
while True:
    print("State?(ENTER to quit)"),
    state = input(">")
    if not state:
        break
    city_found = cities['find'](cities, state)
    print(city_found)
