# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 17:54:33 2022

@author: lbush
"""

print("What is the difference between\n\
a \' and a\"? Or between a \" and a \\\"?")

print("\n")
# transcription program

DNA = "ATTACGGACTCAGTTTGGATC"
print("This is the DNA sequence: ", DNA)
# replace T with U
RNA = DNA.replace("T", "U")
print("This is the RNA sequence: ", RNA)



# print the GC and AT content of a DNA seq
DNA = input("Please enter a DNA sequence: ")

#convert to uppercase
DNA = DNA.upper()

length_seq = len(DNA) #finds the length of the variable DNA
#count the A's and T's and add them together. Do the same for the G's and C's
AT_count = DNA.count("A") + DNA.count("T")
GC_count = DNA.count("G") + DNA.count("C")

#find the percent of the AT and GC regions
AT_perc = (AT_count / length_seq) * 100
GC_perc = (GC_count / length_seq) * 100

# Convert answer to 1 decimal point
AT_perc_1 = "{:.1f}".format(AT_perc)
GC_perc_1 = "{:.1f}".format(GC_perc)

perc = "%"
#print the percents 
print("The A-T content is: ",AT_perc_1,perc)
print("The G-C content is: ",GC_perc_1, perc)


