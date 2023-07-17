# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 06:40:51 2022

@author: lbush

"""

aaList = []
aa = "Phe, Val, Asn, Gln, His, Leu, Cys, Gly, Ser"

aaList = aa.split(', ')

print(aaList)
print("\n")

length = len(aaList)
print(f"The length of the polypeptide is {length} amino acids long\n")

aaList.append("His")
print(aaList)


# create an inversion
# Create an inversion: get two positions in the sequence 
# from the user and invert the sequence of the amino acids between them")

userInput1 = int(input("Please enter the start position of the inversion: "))
userInput2 = int(input("Please enter the end position of the inversion: "))

input1 = userInput1-1
input2 = userInput2

# create a variable named lstSec to store the segment
lstSec = aaList[input1:input2]

# print(lstSec)

# arrange the partial list in reverse order
lstSec.reverse()

print("Amino acid sequence prior to inversion: \n", aaList)

# print(lstSec)
aaList[input1:input2] = lstSec

print("Amino acid sequence after inversion: \n", aaList)


# 2
print("Answers to question number 2")
seqArray = []
seq = "Trp Arg Liu Ilu Asp"
seqArray = seq.split(" ")

print(seqArray)

leng = len(seqArray)

userInput = int(input(f"Please give a number between 1 and {leng}: "))

if (userInput < 1) or (userInput > len(seqArray)):
    print("Error: number not in range")
else:
    print("The amino acid at that position is: ", seqArray[userInput-1])
print("\n")


# 3) Write a program to store the following DNA sequence into an array
print("Answers to question number 3")
#converting string to an array named seqList

seq = "CCGTAACGC"
seqList = []
for i in seq:
    seqList.append(i)

# a) Add a T to the end of the array, then print the array.

seqList.append("T")
print(seqList)

# b) Remove the 1st element of the array and print it.

print(seqList.pop(0))
print(seqList)

# c) Add T to the beginning of the array and print the array.

seqList.insert(0, "T")
print(seqList)





  




