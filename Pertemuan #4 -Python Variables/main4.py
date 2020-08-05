#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 12:46:10 2020

@author: rafliano
"""

# Global Variable
def myfunc():
  global x
  x = "Fantastic"

myfunc()

print("Python Is " + x)


print(20*"=")


x1 = "awesome"

def myfunc():
  global x1
  x1 = "Fantastic"

myfunc()

print("Python Is " + x)