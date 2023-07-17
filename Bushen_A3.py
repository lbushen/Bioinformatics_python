# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 12:17:22 2022

@author: lbush
"""

# Q1

import re

user1 = input("Please enter a file name and extension: ")

# open file and read all but the first line
seq = open(user1, "r")
Seq1 = seq.readlines()[1:]
for i in Seq1:
    s = i.rstrip().upper()
    
# get motif of interest from the user and change it to uppercase
userMotif = input("Please enter a motif of interest: ")
userMotif = userMotif.upper()

def motif_find(sequence):
    if re.search(userMotif,sequence):
        print("n\Motif found \n")
    else:
        print("\nMotif not found \n")
        
motif_find(s)

seq.close()


# Q2
brain = [65, 69, 70, 63, 70, 68]
heart = [102, 95, 98, 110]
lung = [112, 115, 113, 109, 95, 98, 100]

def count(num):
    return len(num)
        
def mean(value):
    ave = sum(value) / len(value)
    return ave
    
def max_val(array):
    return max(array)

def min_val(array):
    return min(array)

def main():
    print("Brain:\n\t count: ", count(brain), "\n\t average enzyme activity: ", mean(brain), "\n\t minimum value: ",min_val(brain), "\n\t Maximum value: ", max_val(brain))
    print("Heart:\n\t count: ", count(heart), "\n\t average enzyme activity: ", mean(heart), "\n\t minimum value: ",min_val(heart), "\n\t Maximum value: ", max_val(heart))
    print("Lung:\n\t count: ", count(lung), "\n\t average enzyme activity: ", mean(lung), "\n\t minimum value: ",min_val(lung), "\n\t Maximum value: ", max_val(lung))

main()   

