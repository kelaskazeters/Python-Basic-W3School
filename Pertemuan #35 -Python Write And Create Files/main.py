#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:09:46 2020

@author: rafliano
"""

# Write to an Existing File
"""
"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
"""
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

# open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

"==================================================="

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())

# Create a New File
# Create a file called "myfile.txt":
f = open("myfile.txt", "x")

"==================================================="

# Create a new file if it does not exist:
f = open("myfile2.txt", "w")
