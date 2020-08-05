#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 15:54:57 2020

@author: rafliano
"""

# Exception Handling
# The try block will generate an error, because x is not defined:

try:
    print(x)
except:
    print("An exception occurred")

# Many Exceptions

# The try block will generate a NameError, because x is not defined:

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# Else

# The try block does not raise any errors, so the else block is executed:

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# Finally
# The finally block gets executed no matter if the try block raises any errors or not:

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

"============================================================="

# The try block will raise an error when trying to write to a read-only file:

# try:
#     f = open("demofile.txt")
#     f.write("Lorum Ipsum")
# except:
#     print("Something went wrong when writing to the file")
# finally:
#     f.close()

# # The program can continue, without leaving the file object open

# # Raise an exception
# x = -1

# if x < 0:
#     raise Exception("Sorry, no numbers below zero")

"============================================================="

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")