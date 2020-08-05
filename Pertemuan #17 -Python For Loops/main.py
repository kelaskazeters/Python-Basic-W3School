#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 23:38:43 2020

@author: rafliano
"""

# Python For Loops
fruits = ["Apel", "Pisang", "Mangga"]
for x in fruits:
    print(x)

# Looping Through A String
for x in "Pisang":
    print(x)

# The Break Statement
fruits = ["Apel", "Pisang", "Mangga"]
for x in fruits:
    print(x)
    if x == "Pisang":
        break

"========================================"

fruits = ["Apel", "Pisang", "Mangga"]
for x in fruits:
    if x == "Pisang":
        break
    print(x)

# The Continue Statement
fruits = ["Apel", "Pisang", "Mangga"]
for x in fruits:
    if x == "Pisang":
        continue
    print(x)

# The range() Function
for x in range(6):
    print(x)

"========================================"

for x in range(2, 6):
    print(x)

"========================================"

for x in range(2, 30, 3):
    print(x)

# Else In For Loop
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# Nested Loops
adj = ["Merah", "Besar", "Berasa"]
fruits = ["Apel", "Pisang", "Mangga"]

for x in adj:
    for y in fruits:
        print(x, y)

# The Pass Statement
for x in [0, 1, 2]:
    pass