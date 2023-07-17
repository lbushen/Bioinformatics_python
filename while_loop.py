# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 07:17:26 2022

@author: lbush
"""
# loop program to guess my name

guess = ""
guess_cap = guess.title()

while (guess_cap != "Lee"):
    guess = input("Please guess my name ")
    guess_cap = guess.title()
    
    
print("That is correct!")
    