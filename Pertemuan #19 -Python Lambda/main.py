#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 19:30:24 2020

@author: rafliano
"""

# Syntax
x = lambda a : a + 10
print(x(5))

"======================================"

x = lambda a, b : a * b
print(x(5, 6))

"======================================"

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Why Use Lambda Functions?
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

"======================================"

def myfunc(n):
    return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

"======================================"

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))