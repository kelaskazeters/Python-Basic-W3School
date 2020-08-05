#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:02:54 2020

@author: rafliano
"""

f = open("demofile.txt", "r")

print(f.read())

# Read Only Parts of the File
f = open("demofile.txt", "r")

print(f.read(5))

# Read Lines
f = open("demofile.txt", "r")

print(f.readline())

"============================================"

f = open("demofile.txt", "r")

print(f.readline())
print(f.readline())

"============================================"

f = open("demofile.txt", "r")
for x in f:
    print(x)

# Close Files
f = open("demofile.txt", "r")

print(f.readline())

f.close()
