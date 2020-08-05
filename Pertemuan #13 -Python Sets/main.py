#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 10:36:38 2020

@author: rafliano
"""

# Set
thisset = {"Apel", "Pisang", "Mangga"}
print(thisset)

# Access Items
thisset = {"Apel", "Pisang", "Mangga"}

for x in thisset:
    print(x)


thisset = {"Apel", "Pisang", "Mangga"}
print("Pisang" in thisset)

# Add Items
thisset = {"Apel", "Pisang", "Mangga"}

thisset.add("Jeruk")

print(thisset)


thisset = {"Apel", "Pisang", "Mangga"}

thisset.update(["Jeruk", "Alpukat", "Anggur"])

print(thisset)

# Get The Length Of A Set
thisset = {"Apel", "Pisang", "Mangga"}

print(len(thisset))

# Remove Item
thisset = {"Apel", "Pisang", "Mangga"}

thisset.remove("Apel")

print(thisset)

"===================================="

thisset = {"Apel", "Pisang", "Mangga"}

thisset.discard("Pisang")

print(thisset)

"===================================="

thisset = {"Apel", "Pisang", "Mangga"}

x = thisset.pop()

print(x)

print(thisset)

"===================================="
thisset = {"Apel", "Pisang", "Mangga"}

thisset.clear()

print(thisset)

"===================================="

thisset = {"Apel", "Pisang", "Mangga"}

del thisset

# Join Two Sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

"===================================="

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# The set() Constructor
thisset = set(("Apel", "Pisang", "Mangga")) # Note Dua Kurung
print(thisset)