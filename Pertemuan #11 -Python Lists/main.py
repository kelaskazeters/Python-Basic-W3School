#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 10:52:57 2020

@author: rafliano
"""

# List
thislist = ["Apel", "Pisang", "Mangga"]
print(thislist)

# Access Items
thislist = ["Apel", "Pisang", "Mangga"]
print(thislist[1])

# Negative Indexing
thislist = ["Apel", "Pisang", "Mangga"]
print(thislist[-1])

# Range of Indexes
thislist = ["Apel", "Pisang", "Mangga", "Jeruk", "Manggis", "Melon", "Nanas"]
print(thislist[2:5])

thislist = ["Apel", "Pisang", "Mangga", "Jeruk", "Manggis", "Melon", "Nanas"]
print(thislist[:4])

thislist = ["Apel", "Pisang", "Mangga", "Jeruk", "Manggis", "Melon", "Nanas"]
print(thislist[2:])

# Range Of Negative Indexes
thislist = ["Apel", "Pisang", "Mangga", "Jeruk", "Manggis", "Melon", "Nanas"]
print(thislist[-4:-1])

# Change Item Value
thislist = ["Apel", "Pisang", "Mangga"]
thislist[1] = "Kiwi"
print(thislist)

# Loop Through A List
thislist = ["Apel", "Pisang", "Mangga"]
for x in thislist:
    print(x)

# Check If Item Exists
thislist = ["Apel", "Pisang", "Mangga"]
if "Mangga" in thislist:
    print("Ya, Ada 'Mangga' Di List Buah")

# List Length
thislist = ["Apel", "Pisang", "Mangga"]
print(len(thislist))

# Add Items
thislist = ["Apel", "Pisang", "Mangga"]
thislist.append("Jeruk")
print(thislist)

thislist = ["Apel", "Pisang", "Mangga"]
thislist.insert(1, "Jeruk")
print(thislist)

# Remove Item
thislist = ["Apel", "Pisang", "Mangga"]
thislist.remove("Apel")
print(thislist)

thislist = ["Apel", "Pisang", "Mangga"]
thislist.pop()
print(thislist)

thislist = ["Apel", "Pisang", "Mangga"]
del thislist[0]
print(thislist)

thislist = ["Apel", "Pisang", "Mangga"]
del thislist

thislist = ["Apel", "Pisang", "Mangga"]
thislist.clear()
print(thislist)

# Copy A List
thislist = ["Apel", "Pisang", "Mangga"]
mylist = thislist.copy()
print(mylist)

thislist = ["Apel", "Pisang", "Mangga"]
mylist = list(thislist)
print(mylist)

# Join Two Lists
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# The List() Constructor
thislist = list(("apple", "banana", "cherry")) # Note Dua Kurung
print(thislist)