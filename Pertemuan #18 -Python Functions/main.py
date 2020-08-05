#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 00:00:43 2020

@author: rafliano
"""

# Creating A Function
def my_function():
    print("Hello From A Function")

# Calling A Function
my_function()

# Arguments
def my_function(fname):
    print(fname + " Paduang")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Number Of Arguments
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Paduang")

"""
If you try to call the function with 1 or 3 arguments, you will get an error:
Example
This function expects 2 arguments, but gets only 1:

def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil")
"""

# Arbitrary Arguments, *args
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Keyword Arguments
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Paduang")

# Default Parameter Value
def my_function(country = "Germany"):
    print("I am from " + country)

my_function("Swedia")
my_function("Indonesia")
my_function()
my_function("Brazil")

# Passing A List As An Argument
def my_function(food):
    for x in food:
        print(x)

fruits = ["Apel", "Pisang", "Mangga"]

my_function(fruits)

# Return Values
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# The Pass Statement
def myfunction():
    pass

myfunction()

# Recursion
def tri_recursion(k):
    if(k>0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)