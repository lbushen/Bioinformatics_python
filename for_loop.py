# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 07:42:30 2022

@author: lbush
"""
# program to add and average 5 numbers from user input using a for loop

# initialize variable
sum = 0
# get user input 5 times using range function
for num in range(0, 5):
    num = int(input("Please enter a number: "))
    sum = sum + num

print("\n")
print("The sum of the numbers entered is: ", sum)

# take average of the 5 numbers
ave = sum/5

print("The average of the numbers entered is: ", ave)