#Project
import re
import os
file = open(input('Please enter the file to be analyzed '))
headers = []
sequences = []
reverse = []
#function for placing headers and sequences into arrays
def files_to_lists():
    read_headers = file.read().split('\n')
    sequence_line = ''
    for x in read_headers:
        if x.startswith('>'):
            x.rstrip('\n')
            headers.append(x)
            if sequence_line != '':
                sequences.append(sequence_line.upper())
        else:
            sequence_line += x.strip().upper()
    sequences.append(sequence_line.upper())
    print(headers)
    print(sequences)
files_to_lists()
#function containing code to reverse sequences
def reverse_sequences():
    for sequence in sequences:
        reverse.append(sequence[::-1])
    print(reverse)
reverse_sequences()
#function containing the conversion of headers and sequences into a dictionary (if we need it), with headers as the keys
def lists_to_dictionary():
    dictionary = dict(zip(headers, sequences))
    print(dictionary)
lists_to_dictionary()
#default ORF length is 50bp
ORF_length = int(input('Enter the minimum ORF length: '))
# if ORF_length < 50:  # I think we needed a conditional here - Lee
#     print("Please input a length greater than 50")

start_codon = re.compile(r'ATG')
stop_codons = re.compile(r'(TAA)|(TAG)|(TGA)')


def ORF(value):   
    target_seq = re.compile(r'(ATG(?:...)*?(?=TAG|TGA|TAA))') 
    for match in re.finditer(target_seq, value):
        position = match.start()
        for start in range(0, 3):
            x = match.group()[start::]
            if len(x) > ORF_length:
                codon = ' '.join(x[i:i+3] for i in range(0,len(x),3))
                print("FRAME=", start+1, " | POS=", position, " | LEN=" ,len(x))
                print(codon)
            start += 1

# for some reason this is not working.  
# I thought the name of the dictionary was dictionary but I am getting an error that
# 'dictionary' is undefined
for key, value in dictionary.items():
    print(key)    
    ORF(value)




    
    
