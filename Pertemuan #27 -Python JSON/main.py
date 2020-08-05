#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 20:20:58 2020

@author: rafliano
"""

# JSON In Python
import json

# some JSON:
x =  '{ "name":"Rafli", "age":10, "city":"Jakarta"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# Convert From Python To JSON
import json

# a Python object (dict):
x = {
  "name": "Rafli",
  "age": 10,
  "city": "Jakarta"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

"==========================================="

import json

print(json.dumps({"name": "Rafli", "age": 10}))
print(json.dumps(["Apel", "Pisang"]))
print(json.dumps(("Apel", "Pisang")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

"==========================================="

import json

x = {
  "name": "Rafli",
  "age": 10,
  "Writer": False,
  "Programmer": True,
  "Programming Language": ("Python","Php"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# Format The Result
import json

x = {
  "name": "Rafli",
  "age": 10,
  "Writer": False,
  "Programmer": True,
  "Programming Language": ("Python","Php"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))

"==========================================="

import json

x = {
  "name": "Rafli",
  "age": 10,
  "Writer": False,
  "Programmer": True,
  "Programming Language": ("Python","Php"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))

# Order The Result
import json

x = {
  "name": "Rafli",
  "age": 10,
  "Writer": False,
  "Programmer": True,
  "Programming Language": ("Python","Php"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))