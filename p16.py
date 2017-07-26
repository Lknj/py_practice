from sys import argv
script,filename = argv
print("%r" %filename)
target = open(filename)
print(target.read())
