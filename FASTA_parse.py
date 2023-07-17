# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 21:11:38 2022

@author: lbush
"""
import re
fasta = open("glycine.txt", "r")

line1 = fasta.readline()
print(line1)

accnString = re.split('[>+ ]', line1)
accn = accnString[1]

print(accn)



