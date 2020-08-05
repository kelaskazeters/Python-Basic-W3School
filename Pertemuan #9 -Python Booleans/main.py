#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 09:33:12 2020

@author: rafliano
"""

# Booleans Values
print(10 >= 9)
print(10 == 9)
print(10 <= 9)

a = 200
b = 33

if b >= a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Evaluate Values and Variables
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Most Values Are True
print(bool("abc"))
print(bool(123))
print(bool(["Apel", "Mangga", "Pisang"]))

# Some Values are False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# Functions Can Return A Boolean
x = 200
print(isinstance(x, int))
