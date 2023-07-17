#Project
import re
import os
file = open(input('Please enter the file to be analyzed '))
headers = []
sequences = []
parsing = []
#function for placing headers and sequences into arrays
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
#added the below to seperate the combined sequences
    length = 0
    longest_sequence = max(parsing, key = len)
    for position in parsing:
        repeats_removed = position[length:]
        sequences.append(repeats_removed)
        length = len(position)
    print(headers)
    print(sequences)
files_to_lists()
#function containing the conversion of headers and sequences into a dictionary (if we need it), with headers as the keys
seq_dict = dict(zip(headers, sequences))
#default ORF length is 50bp
ORF_length=50
user_ORF_len=int(input('Enter the minimum ORF length: '))
if user_ORF_len>ORF_length:
    ORF_length=user_ORF_len

#Look for ORFs
for value in seq_dict.values():
    m123=re.finditer(r'(ATG(?:...)*?(?=TAG|TGA|TAA))', value)
    #Loop through the regex result
    for match1 in m123:
        seq_name =[key for key, val in seq_dict.items() if val == value]
      #FRAMES 1,2,3
        #begining of the ORF
        start1=match1.start()
        #end of the ORF
        end1= match1.end()
        #length of ORF is start subtracted from end
        length1= end1-start1
        #Print only the ORFs that are larger than ORF_length
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
            print(seq_name[0]+" | FRAME= "+str(frame1)+" | POS= "+ str(pos1)+" | LEN= "+str(length1)+ "\n"+match1.group(0))
    
    #FRAMES 4,5 and 6
    #generate the reverse complement
    revseq=value[::-1].replace("A", "t").replace("G", "c").replace("T", "a").replace("C", "g").upper()
    #For frames 4, 5, and 6
    m456=re.finditer(r'(ATG(?:...)*?(?=TAG|TGA|TAA))', revseq )
    for match2 in m456:
        start2=match2.start()
        end2= match2.end()
        length2= end2-start2
        if length2>ORF_length:
            pos2=match2.start()*(-1)
            if pos2%3==-1:
                frame2=4
            elif pos2%3==-2:
                frame2=5
            elif pos2%3==0:
                frame2=6
            print(seq_name[0]+" | FRAME= "+str(frame2)+" | POS= "+ str(pos2)+" | LEN= "+str(length2)+"\n"+match2.group(0))
