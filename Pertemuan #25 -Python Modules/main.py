#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 22:17:35 2020

@author: rafliano
"""

# Use A Module
import mymodule

mymodule.greeting("Rafli")

a = mymodule.person1["age"]
print(a)

# Renaming A Module
import mymodule as mx

a = mx.person1["age"]
print(a)

# Built-in Modules
import platform

x = platform.system()
print(x)

# Using The dir() Function
import platform

x = dir(platform)
print(x)