# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 07:31:08 2022

@author: lbush
"""

import re

# userFile = input("PLease enter file name and extension: ")
fasta = open("dna.txt", "r").read().strip("\n")
cuts = [0]
for match in re.finditer(r"A[ATGC]TAAT", fasta):
    cuts.append(match.start() + 3)
cuts.append(len(fasta))
print(cuts)

sortedCuts = sorted(cuts)
'''
for i in range(1,len(sortedCuts)):
    this_cut_position = sortedCuts[i]
    previous_cut_position = sortedCuts[i-1]
    fragment_size = this_cut_position - previous_cut_position
    print("one fragment size is " + str(fragment_size))
'''