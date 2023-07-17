# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:41:21 2022

@author: lbush
"""
import os
import re

# Q1
user = input("Please enter a filename that is in FASTA format: ")

# file not found function
def filefound(file):
    file_open = open(file).read()
    count = 0
    while count < 5:
        found = False
        
        if file in os.listdir(".") and file_open.startswith(">"):
            found = True
            
            # file.close()
            break
            
        else:
            count += 1
    if found == False:
        print("\nYou did not enter a valid filename or file not in FASTA format.") 

filefound(user)

def strip_seq(user): # to strip the file so only have sequence
    accn_file = open(user).read()
    accn = re.search(r'(>)(.+)', accn_file)
    file = accn_file.strip(accn.group())
    return file

def count_n(user): # find the nucleotide count
    file = strip_seq(user)
    count_T = file.count("T")
    count_A = file.count("A")
    count_G = file.count("G")
    count_C = file.count("C")
    count_N = file.count("N")
    print("The sequence contains",count_T,"\"T\"s")
    print("The sequence contains",count_A,"\"A\"s")
    print("The sequence contains",count_G,"\"G\"s")
    print("The sequence contains",count_C,"\"C\"s")
    print("The sequence contains",count_N,"unknown nucleotides")
          
def A_T(user): # to find the AT content
    file = strip_seq(user)
    count_T = file.count("T")
    count_A = file.count("A")
    seq_length = len(file)
    AT_content = ((count_T + count_A)/seq_length) * 100
    return AT_content
    
def G_C(file): # to find the GC content
    file = strip_seq(user)
    count_G = file.count("G")
    count_C = file.count("C")
    seq_length = len(file)
    GC_content = (((count_G) + (count_C))/seq_length) * 100
    return GC_content
        
def comp(file): # to find the complement
    file = strip_seq(user)
    temp1 = file.replace('A','t')
    temp2 = temp1.replace('T','a')
    temp3 = temp2.replace('C','g')
    temp4 = temp3.replace('G','c')
    return temp4
    
def rev_comp(file): # to find the reverse complement
    file = strip_seq(user)
    temp1 = file.replace('A','t')
    temp2 = temp1.replace('T','a')
    temp3 = temp2.replace('C','g')
    temp4 = temp3.replace('G','c')
    rev_file = temp4[::-1].upper().lstrip('\n')
    return rev_file
    
user_choice = int(input("Chose from the follow:\n\
                    (1) count nucleotides\n\
                    (2) find A-T content\n\
                    (3) find G-C content\n\
                    (4) find complement\n\
                    (5) find reverse complement\n\
                        : "))
        
if user_choice == 5:
    print("The reverse complement is: ", rev_comp(user))

if user_choice == 4:
    print("The complement is: ", comp(user))
    
if user_choice == 3:
    print("The G-C content of the sequence is", G_C(user),"%" )
    
if user_choice == 2:
    print("The A-T content of the sequence is", A_T(user),"%" )

if user_choice == 1:
    count_n(user)
    
# Q2

user2 = input("Please enter a filename that is in FASTA format: ")

filefound(user2)  

user_frame = int(input("Please select an open reading frame.  1-6: " ))

# dictionary of codons and amino acids
gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

# translate_dna function from Jones (2013) Python for Biologists
def translate_dna(dna):
    last_codon_start = len(dna)-2
    protein = ""
    for start in range(0, last_codon_start, 3):
        codon = dna[start:start+3]
        aa = gencode.get(codon, 'X')
        protein = protein + aa
    return protein

seq = strip_seq(user)
rev_seq = rev_comp(user)

i = (user_frame - 1)
if 0 <= i <= 2: # for the forward stand
    print(f"The translation at frame {user_frame} is: ", translate_dna(seq[i::]))
if 3 <= i <= 5: # for the reverse complement strand
    rev_i = i - 2
    print(f"The translation at frame {user_frame} is: ", translate_dna(rev_seq[rev_i::]))
    
# Q3

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
    file_open = open(accession[i]+"txt", "w").write(">"+accession[i]+" "+info[i]+"\n"+(sequence[i]+"\n"))

#Q4
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

# Q5

# I could not figure out how to iterate over all the values to 
# sum them up. 

file = open("genome.txt").read().strip("\n")

ls = []
for seq in re.finditer(r"([AGTC].*)", file):
    ls.append(seq.group(0))

genome = ''.join(ls)

# cut genome based on frames    
fr1 = genome[0::]
fr2 = genome[1::]
fr3 = genome[2::]

fr_dict={}
fr_total = {}

# modified from Jones (2013) Python for Biologists
for base1 in ['A', 'T', 'G', 'C']:
    for base2 in ['A', 'T', 'G', 'C']:
        for base3 in ['A', 'T', 'G', 'C']:
            trinucleotide = base1 + base2 + base3
            # find the count for each trinucleotide in each frame
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

 
   

    
    

        
    