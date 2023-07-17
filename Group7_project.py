#Project
import re
import os
#open file #Vienna
file = open(input('Please enter the file to be analyzed: '))
#arrays for holding header, sequences, and parsing lines #Vienna
headers = []
sequences = []
parsing = [] 
#function for placing headers and sequences into arrays #Vienna
def files_to_lists(): 
    read_headers = file.read().split('\n')
    sequence_line = ''
    for x in read_headers:
        if x.startswith('>'):
            x.rstrip('\n')
            headers.append(x)
            if sequence_line != '':
                parsing.append(sequence_line.upper())
        else:
            sequence_line += x.strip().upper()
    parsing.append(sequence_line.upper())
    length = 0
    longest_sequence = max(parsing, key = len)
    for position in parsing:
        repeats_removed = position[length:]
        sequences.append(repeats_removed)
        length = len(position)
files_to_lists()

#function containing the conversion of headers and sequences into a dictionary (if we need it), with headers as the keys #Vienna
seq_dict = dict(zip(headers, sequences))

#default ORF length is 50bp. Ask user for ORF length, if user provides more than 50 use that value else use 50 #Nabin
ORF_length=50
user_ORF_len=int(input('Enter the minimum ORF length: '))
if user_ORF_len>ORF_length:
    ORF_length=user_ORF_len

# Lee - function to separate orf into codons and print 15 codons per line        
def codon15(x):
    c_ls = [] # put codons into a list
    for i in range(0,len(x),3):
        codon = (x[i:i+3])  # https://stackoverflow.com/questions/37101101/convert-sequences-in-codons
        c_ls.append(codon)
    # initialize variables to print 15 codons per line
    a = 0
    b = 15  
    for i in c_ls:
        codonline = ' '.join(c_ls[a:b]) #join 15 codons per line
        print(codonline)
        if len(codonline) < 58:  # '58' is less than the number of chars / line
            break   
        else:
            a += 15
            b += 15
        
#Look for ORFs #code by Nabin
for value in seq_dict.values():
    m123=re.finditer(r'(ATG(?:...)*?(?=TAG|TGA|TAA))', value) #https://stackoverflow.com/questions/40078407/perl-regular-expression-starts-with-atg-and-ends-with-tag-taa-or-tga
    #Loop through the regex result #Nabin
    for match1 in m123:
        seq_name =[key for key, val in seq_dict.items() if val == value]
      #FRAMES 1,2,3  #Nabin
        #begining of the ORF #Nabin
        start1=match1.start()
        #end of the ORF #Nabin
        end1= match1.end()
        #length of ORF is start subtracted from end #Nabin
        length1= end1-start1
        #Print only the ORFs that are larger than ORF_length #Nabin
        if length1>ORF_length:
            #Print position
            pos1=match1.start()
            #Identify frame
            #Frame1
            if pos1%3==1:
                frame1=1
            #Frame2
            elif pos1%3==2:
                frame1=2
            #Frame3
            elif pos1%3==0:
                frame1=3
            fw_frame = match1.group(0)
            print(seq_name[0]+" | FRAME= "+str(frame1)+" | POS= "+ str(pos1)+" | LEN= "+str(length1)),codon15(fw_frame)
    
    #FRAMES 4,5 and 6  #Nabin
    #generate the reverse complement #Nabin
    revseq=value[::-1].replace("A", "t").replace("G", "c").replace("T", "a").replace("C", "g").upper()
    #For frames 4, 5, and 6
    m456=re.finditer(r'(ATG(?:...)*?(?=TAG|TGA|TAA))', revseq )
    for match2 in m456:
        start2=match2.start()
        end2= match2.end()
        length2= end2-start2
        if length2>ORF_length:
            pos2=match2.start()*(-1)
            if pos2%3==1:
                frame2=4
            elif pos2%3==2:
                frame2=5
            elif pos2%3==0:
                frame2=6
            rev_frame = match2.group(0)
            print(seq_name[0]+" | FRAME= "+str(frame2)+" | POS= "+ str(pos2)+" | LEN= "+str(length2)),codon15(rev_frame)

    
