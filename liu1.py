# coding:utf-8


months = [
    'Jannary',
    'February',
    'March',
    'Aprll',
    'May',
    'June',
    'July',
    'Augest',
    'September',
    'October',
    'November',
    'December'
]

# 以1~31的数字作为结尾的列表
endings = ['st','nd','rd'] + 17 * ['th'] \
          + ['st', 'nd', 'rd'] + 7 * ['th'] \
          + ['st']

year = input('Year: ')

month = input('Month: ')

day = input("Day: ")

month_number = int(month)
day_number = int(day)

# 要将月份和天数减1， 已获得正确索引
month_name = months[month_number - 1]
ordinal = day + endings[day_number - 1]

print(month_name + ' ' + ordinal + '. ' + year)
