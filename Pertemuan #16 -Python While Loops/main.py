#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 23:31:27 2020

@author: rafliano
"""

# The While Loop
i = 1
while i < 6:
    print(i)
    i += 1

# The Break Statement
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# The Continue Statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# The Else Statement
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")