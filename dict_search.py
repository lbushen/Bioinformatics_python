# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 22:15:03 2022

@author: lbush
"""

'''
Write a program that asks a user for a gene ID or accession number 
and returns the sequence that corresponds to that gene. Use a 
dictionary to accomplish this. Get the genes and their sequences 
from NCBI and create the dictionary so that the key = gene ID and 
value = sequence. Handle the case where the gene ID is not found in 
the dictionary. 
'''

user = input("Please provide a gene id or accession number: ")

geneids = {
    '>NM_000207.3 Homo sapiens insulin (INS), transcript variant 1, mRNA':'\
    AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGATCACTGTCCTTCTGCCATGGCCCTGTG\
    GATGCGCCTCCTGCCCCTGCTGGCGCTGCTGGCCCTCTGGGGACCTGACCCAGCCGCAGCCTTTGTGAAC',
    '>K02233.1 Guinea pig insulin gene, complete cds':'CTGCAGACCCAGCACCAGGGAAA\
    TGATCCAGAAATTGCAACCTCAGCCCCCTGGCCATCTGCTGATGCCA\
    CCACCCCCAGGTCCCTAATGGGCCTGGTGGCAGAGTTTGGGAAGATGGGCTCAGGGCTATATAAAGTCCA',
    '>AY823483.1 Octodontomys gliroides voucher SSUC-Ma 00196 insulin gene, \
    partial cds':'TATTCCAGCCAGCACCTGTGTGGCTCCAACCTAGTGGAGGCGCTGTACATGACATGTGGA\
    CATAATGGCTTCTATAGGCCCAACGACGGCATTGTGGATCAGTGCTGTAATAACATCTGCACATTTAACCAGCTG\
    CAGAACTACTGCAATGTCCCTTAG'
    }
    
x = 0      
for key, value in geneids.items():
    if user in key:
        x = 1
        
if x == 1:
    print(value)
else:
    print("Accesion number not found")
 
    

          

