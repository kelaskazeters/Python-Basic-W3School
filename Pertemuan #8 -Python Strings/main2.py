#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 21:58:55 2020

@author: rafliano
"""

# Strings Are Arrays
a = "Hello World!"
print(a[1])

# Slicing
b = "Hello World!"
print(b[2:5])

# Negative Indexing
b = "Hello World!"
print(b[-5:-2])

# String Length
a = "Hello World!"
print(len(a))

# String Methods
a = " Hello World! "
print(a.strip()) # Returns "Hello World!"

a = "Hello World!"
print(a.lower())

a = "Hello World!"
print(a.upper())

a = "Hello World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# Check String
txt = "The Rain In Spain Stays Mainly In The Plain"
x = "ain" in txt
print(x)

txt = "The Rain In Spain Stays Mainly In The Plain"
x = "ain" not in txt
print(x)

# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

# Add Space Between Them
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# String Format
umur = 10
txt = "Nama Saya Rafli, Umur Saya {}"
print(txt.format(umur))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))