# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 05:49:56 2022

@author: lbush
"""
# program for accessing items in an array

# the string 
things = "peroxidase,gene,protein,oxidase,hemoglobin"

# creating an array from the string
array = things.split(",")

# print 3rd element
print(array[2])

print("\n")

# print 5 element of array
print(array[4])