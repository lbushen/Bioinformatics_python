# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 22:08:31 2022

@author: lbush
"""
# program to determine if a number is even or odd
# get input from user
num = int(input("Please enter a number: "))

# if the number is divided by 2 and remainder not equal to zero it is odd
if num % 2 != 0:
    print("Number is odd")
else:
    print("Number is even")
    