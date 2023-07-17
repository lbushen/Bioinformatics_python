# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 21:39:16 2022

@author: lbush
"""
# list of amino acids


AA_list = ["Trp", "Arg", "Liu", "Ilu", "Asp"]

#ask user for input
user_aa = input("Please give a 3 letter amino acid abbreviation: ")

# ensure format is identical for list and user
user_aa = user_aa.title()

tf = 0
# loop through AA_list to find the user input

for aa in AA_list:
    if aa == user_aa:
        tf = 1

if tf == 1:
    print("Amino acid found")
else:
    print("Amino acid NOT found") 
      

# for aa in range(len(AA_list)):
#     if AA_list[aa] == user_aa:
#         print("Amino acid found")
#     else:
#         print("Amino acid NOT found") 
#     break
# yes = user_aa in AA_list

#if the user input was found or if yes was true.  If not true.
# if yes == True:
#     print("Amino acid found")
# else:
#     print("Amino acid NOT found")       
        
