#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 12:50:31 2020

@author: rafliano
"""

"""
Text Type        :   str
Numeric Types    :   int, float, complex
Sequence Types   :   list, tuple, range
Mapping Type     :	 dict
Set Types        :	 set, frozenset
Boolean Type     :	 bool
Binary Types     :	 bytes, bytearray, memoryview

"""

x1 = "Hello World!" # Data Str
x2 = 20 # Data Int
x3 = 20.5 # Data Float
x4 = 1j # Data Complex	
x5 = ["Apel", "Pisang", "Mangga"] # Data List	
x6 = ("Apel", "Pisang", "Mangga") # Data Tuple
x7 = range(6) # Data Range	
x8 = {"Nama" : "Rafli", "Umur" : 10}	# Data Dict	
x9 = {"Apel", "Pisang", "Mangga"} # Data Set	
x10 = frozenset({"Apel", "Pisang", "Mangga"})	# Data Frozenset	
x11 = True # Data Bool
x12 = b"Hello" # Data Bytes	
x13 = bytearray(5) # Data Bytearray
x14 = memoryview(bytes(5)) # Data Memoryview