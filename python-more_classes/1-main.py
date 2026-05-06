#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)


my_rectangle.width = 2
my_rectangle.height = 4
print(my_rectangle.__dict__)

try:
    print(my_rectangle.__dict__)
except Exception as e:
    print(e)

print("--")

try:
    my_rectangle.width = -2
    my_rectangle.height = 4
    print(my_rectangle.__dict__)
except Exception as e:
    print(e)

print("--")

try:
    my_rectangle.width = 2
    my_rectangle.height = -4
    print(my_rectangle.__dict__)
except Exception as e:
    print(e)

print("--")

try:
    my_rectangle.width = "test"
    my_rectangle.height = 4
    print(my_rectangle.__dict__)
except Exception as e:
    print(e)

print("--")


try:
    my_rectangle.width = 2
    my_rectangle.height = "test"
    print(my_rectangle.__dict__)
except Exception as e:
    print(e)

print("--")