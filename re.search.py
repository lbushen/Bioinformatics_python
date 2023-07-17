# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 21:46:37 2022

@author: lbush
"""
import re

rna = "Several rapidly developing RNA interference (RNAi) \
methodologies hold the promise to selectively inhibit gene expression in \
mammals. RNAi is an innate cellular process activated when a \
double-stranded RNA (dsRNA) molecule of greater than 19 duplex \
nucleotides enters the cell, causing the degradation of not only the \
invading dsRNA molecule, but also single-stranded (ssRNAs) RNAs of \
identical sequences, including endogenous mRNAs."

r = re.search(r"RNAi", rna)
d = re.search(r"dsRNA", rna)
s = re.search(r"ssRNAs", rna)
m = re.search(r"mRNAs.", rna)

print("(RNAi) ends at position",str(r.end()))
print("(dsRNA) ends at position",str(d.end()))
print("(ssRNAs) ends at position",str(s.end()))
print("mRNAs. ends at position",str(r.end()))