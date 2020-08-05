#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 21:16:03 2020

@author: rafliano
"""

# Create A Class
class MyClass:
    x = 5

print(MyClass)

# Create Object
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

# The __init__() Function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Rafli", 10)

print(p1.name)
print(p1.age)

# Object Methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello My Name Is " + self.name)

p1 = Person("Rifqi", 13)
p1.myfunc()

# The self Parameter
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello My Name Is " + abc.name)

p1 = Person("Zaki", 4)
p1.myfunc()

# Modify Object Properties
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("Rafli", 10)

p1.age = 15

print(p1.age)

# Delete Object Properties
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("Linus", 36)

del p1.age

# Delete Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("Jamil", 56)

del p1

# The pass Statement
class Person:
    pass