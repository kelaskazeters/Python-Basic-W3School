#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:23:56 2020

@author: rafliano
"""

# Delete a File
import os
os.remove("demofile.txt")

# Check if File exist:
import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

# Delete Folder
import os
os.rmdir("myfolder")

# Note: You can only remove empty folders.
