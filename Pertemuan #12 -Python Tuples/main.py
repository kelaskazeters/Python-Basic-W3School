#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 11:50:45 2020

@author: rafliano
"""

# Tuple
thistuple = ("Apel", "Pisang", "Mangga")
print(thistuple)

# Access Tuple Items
thistuple = ("Apel", "Pisang", "Mangga")
print(thistuple[1])

# Negative Indexing
thistuple = ("Apel", "Pisang", "Mangga")
print(thistuple[-1])

# Range Of Indexes
thistuple = ("Apel", "Pisang", "Mangga", "Jeruk", "Manggis", "Melon", "Nanas")
print(thistuple[2:5])

# Range Of Negative Indexes
thistuple = ("Apel", "Pisang", "Mangga", "Jeruk", "Manggis", "Melon", "Nanas")
print(thistuple[-4:-1])

# Change Tuple Values
x = ("Apel", "Pisang", "Mangga")
y = list(x)
y[0] = "Alpukat"
x = tuple(y)

print(x)

# Loop Through A Tuple
thistuple = ("Apel", "Pisang", "Mangga")
for x in thistuple:
    print(x)

# Check if Item Exists
thistuple = ("Apel", "Pisang", "Mangga")
if "Apel" in thistuple:
    print("Ya, Ada 'Apel' Di Tuple Buah")

# Tuple Length
thistuple = ("Apel", "Pisang", "Mangga")
print(len(thistuple))

# Create Tuple With One Item
thistuple = ("Apel",)
print(type(thistuple))

# NOT a tuple
thistuple = ("Apel")
print(type(thistuple))

# Remove Tuple
thistuple = ("Apel", "Pisang", "Mangga")
del thistuple

# Join Two Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# The tuple() Constructor
thistuple = tuple(("Apel", "Pisang", "Mangga")) # Note Dua Kurung 
print(thistuple)