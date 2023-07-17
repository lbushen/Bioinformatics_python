# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 09:55:32 2022

@author: lbush
"""

import re


user_gb = input("Please enter GenBank file: ")

gb_info = open(user_gb).read()

# modified from Nabin Poudel week 11 discussion
accession=[]
info=[]
sequence=[]

for match1 in re.finditer(r'(ACCESSION)(\s+)(.+)', gb_info):
    accession.append(match1.group(3))
for match2 in re.finditer(r'(DEFINITION)\s+(\w+(\.)?.+)', gb_info):
    info.append(match2.group(2))
seq_remove_newline=re.sub("\n", "", gb_info)
seq_remove_space=re.sub(" ", "", seq_remove_newline)
numbers = r'\d'
seq_remove_number=re.sub(numbers, "", seq_remove_space)
for match3 in re.finditer(r'(ORIGIN)(\w+)(\/\/)', seq_remove_number):
    sequence.append(match3.group(2).upper())
 
for i in range (0, len(accession)):
    file_open = open(accession[i]+".txt", "w").write(">"+accession[i]+" "+info[i]+"\n"+(sequence[i]+"\n"))



    


# print(gb_seq.group())   


