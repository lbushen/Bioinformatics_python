# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 13:39:50 2022

@author: lbush
"""
#  Q1
import re

# ask user for filename and open file
user = input("Enter file name: ")
userinput = open(user).read()

# function for conditional if AT is found repeating 3 or more times in the file
def AT_search(string):
    if re.search(r"((AT){3,})", string):
        print("The AT repeat exists in the sequence.")
        
    else:
        print("The AT repeat does not exists in the sequence.")
       

# calling the function              
AT_search(userinput)



# Q2

# open EMBL file and readlines
file = open("EMBL_records.txt", "r")
emb_file = file.readlines()

# function to loop through file to print lines that start with these strings
def embl(rec):
    for line in rec:
        if line.startswith("ID"):
            print(line)
        if line.startswith("DE"):
            print(line)
        if line.startswith("SQ"):
            print(line)
        if line.startswith(" "):
            print(line)

# call function
embl(emb_file)



