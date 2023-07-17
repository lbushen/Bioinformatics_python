# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 23:15:19 2022

@author: lbush
"""

# background_frq(codon) = 100 * N(codon)/ Total_codons   
# N(codon): the number of occurrence of the codon across the entire genome, 
# Total_codons:the total number of all codons in the whole genome.

 # Print out the background frequency of each codon, from AAA to TTT. 
 # Use a dictionary in your solution.
 
import re
file = open("dna2.txt").read().strip("\n")

ls = []
for seq in re.finditer(r"([AGTC].*)", file):
    ls.append(seq.group(0))

genome = ''.join(ls)
    
fr1 = genome[0::]
fr2 = genome[1::]
fr3 = genome[2::]

fr_dict={}
fr_total = {}

for base1 in ['A', 'T', 'G', 'C']:
    for base2 in ['A', 'T', 'G', 'C']:
        for base3 in ['A', 'T', 'G', 'C']:
            trinucleotide = base1 + base2 + base3
            total = fr1.count(trinucleotide)+fr2.count(trinucleotide)+fr3.count(trinucleotide)
            average = total/3
            if average > 0:
                fr_total[trinucleotide] = total
                fr_dict[trinucleotide] = average
                for trinucleotide, total in fr_total.items():
                    sum_values = sum(total)
                bk_frq = 100 * total/sum_values
                fr_dict[trinucleotide] = bk_frq
                
print(fr_dict)

# I could not figure out how to iterate over all the values to 
# sum them up.  