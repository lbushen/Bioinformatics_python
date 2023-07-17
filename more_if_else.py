# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 22:28:15 2022

@author: lbush
"""
# program for the user to guess my name correctly

my_name = "Lee"

guess = input("Please guess my name ")

# ensure the first letter of the name the user inputted is capitalized
guess_cap = guess.title()

# conditional to see if the name user guessed is correct
if guess_cap == my_name:
    print("Well done, good guess work!")
else:
    print("Try again next time!")