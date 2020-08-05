#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 21:58:15 2020

@author: rafliano
"""

# Iterator Vs Iterable

# Iterator From A Tuple
mytuple = ("Apel", "Pisang", "Mangga")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Iterable From Strings
mystr = "Mangga"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Looping Through An Iterator
mytuple = ("Apel", "Pisang", "Mangga")

for x in mytuple:
    print(x)

"============================================"

mystr = "Pisang"

for x in mystr:
    print(x)

# Create An Iterator
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# StopIteration
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)