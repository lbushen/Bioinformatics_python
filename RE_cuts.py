# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 08:55:11 2022

@author: lbush
"""
import re

RE_file = open("RestrictionEnzymes.txt").read().strip("\n")

# initialize lists to zip later into a dictionary
RE=[]
cuts=[]

# parse out  the restriction enzyme name and put it into RE list
for res in re.finditer(r"(\w*)(,)(.*)", RE_file):
    RE.append(res.group(1))
# parse out the restriction enzyme sequence and put into cuts list    
for cut in re.finditer(r"(\w*)(,)(.*)", RE_file):
    cuts.append(cut.group(3))

# create a dictionary by zipping the lists    
RE_dict = dict(zip(RE, cuts))
      
user = input("Please enter a file containing a nucleotide sequence: ")
seq = open(user).read()

enzyme = input("Please enter the name of an enzyme to cut with: ")
cut_site = RE_dict[enzyme]

# find the position of the ' in the value of RE_dict
ap = RE_dict[enzyme].find("'")
# replace the ' with ""
strip_cut = cut_site.replace("\'", "")
# to find the cut site
cut_start = len(strip_cut) - ap

# for single letter codes: 
# https://www.promega.com/resources/guides/nucleic-acid-analysis/restriction-enzyme-resource/

nuc_sub1 = re.sub("R","[AG]", strip_cut)
nuc_sub2 = re.sub("N","[GCTA]",nuc_sub1)
nuc_sub3 = re.sub("W", "[AT]", nuc_sub2)
nuc_sub4 = re.sub("Y", "[CT]",  nuc_sub3)
nuc_sub5 = re.sub("K", "[GT", nuc_sub4)
nuc_sub6 = re.sub("S", "[GC]", nuc_sub5)
nuc_sub7 = re.sub("M", "[AC]", nuc_sub6)
nuc_sub8 = re.sub("B", "[TGC]", nuc_sub7)
nuc_sub9 = re.sub("H", "[ACT]", nuc_sub8)
nuc_sub10 = re.sub("D", "[AGT]", nuc_sub9)
nuc_sub11 = re.sub("V", "[AGC]", nuc_sub10)

# initialize cuts2 list
cuts2=[0]

# loop through seq to find nuc_sub11 and cut from the end 
for match in re.finditer(nuc_sub11, seq):
    cuts2.append(match.end() - ap)
cuts2.append(len(seq))
# trim the first and the last item in the cuts2 list
del cuts2[0]
del cuts2[-1]
# join_cuts2 = ','.join(cuts2[1:-2]) : not working for some reason

print(f"The enzyme {enzyme} cuts at position(s) {cuts2} ")



  
    
    
    

