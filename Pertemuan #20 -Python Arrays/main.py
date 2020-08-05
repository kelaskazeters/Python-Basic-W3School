#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 19:35:18 2020

@author: rafliano
"""

cars = ["Ford", "Volvo", "BMW"]

print(cars)

# Access The Elements Of An Array
cars = ["Ford", "Volvo", "BMW"]

x = cars[0]

print(x)

# Modify the value
cars = ["Ford", "Volvo", "BMW"]

cars[0] = "Toyota"

print(cars)

# The Length Of An Array
cars = ["Ford", "Volvo", "BMW"]

x = len(cars)

print(x)

# Looping Array Elements
cars = ["Ford", "Volvo", "BMW"]

for x in cars:
    print(x)

# Adding Array Elements
cars = ["Ford", "Volvo", "BMW"]

cars.append("Honda")

print(cars)

# Removing Array Elements
cars = ["Ford", "Volvo", "BMW"]

cars.pop(1)

print(cars)

"======================================"

cars = ["Ford", "Volvo", "BMW"]

cars.remove("Volvo")

print(cars)
