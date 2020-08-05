#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 22:33:09 2020

@author: rafliano
"""

# Python Dates
import datetime

x = datetime.datetime.now()
print(x)

# Date Output
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# Creating Date Objects
import datetime

x = datetime.datetime(2020, 5, 15)

print(x)

# The strftime() Method
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))