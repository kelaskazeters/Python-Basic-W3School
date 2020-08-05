#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 18:43:07 2020

@author: rafliano
"""

x = 1    # Int
y = 2.8  # Float
z = 1j   # Complex
print(type(x))
print(type(y))
print(type(z))

print("\n")

# Int
print("Int")
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

print("\n")

# Float
print("Float")
u = 1.10
v = 1.0
w = -35.59
x = 35e3
y = 12E4
z = -87.7e100
print(type(u))
print(type(v))
print(type(w))
print(type(x))
print(type(y))
print(type(z))

print("\n")

# Complex
print("Complex")
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

print("\n")

# Mengubah Tipe Data
print("Mengubah Tipe Data")
"""
Method Untuk Mengubah Tipe Data :
int()
float()
complex()
"""
x = 1 # Int
y = 2.8 # Float
z = 1j # Complex

# Convert From Int To Float :
a = float(x)

# Convert From Float To Int :
b = int(y)

# Convert From Int To Complex :
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

print("\n")

# Random Number
print("Random Number")
import random

print(random.randrange(1,10))