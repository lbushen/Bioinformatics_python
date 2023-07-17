#Project
import re
#open file
file = open(input('Please enter the file to be analyzed '))
#array for header
headers = []
#array for sequences
sequences = []

#parsing out headers and sequences into arrays
morelines = True
while morelines: #if there are morelines
    seq=""
    moreseq = True 
    #if there are more sequences
    while moreseq:
        #read next line
        nxtline = file.readline()
        #if no more lines
        if not nxtline:
        #tell machine that there are not more lines
            morelines = False
            break
        #if the next line does not start with a >
        elif nxtline[0] != ">":
        #strip that line
            seq+=nxtline.strip()
        #if next line starts with else
        else: 
            headers.append(nxtline.strip())
            moreseq = False  
    sequences.append(seq.upper())
sequences=sequences[1:]


#function containing the conversion of headers and sequences into a dictionary (if we need it), with headers as the keys
seq_dict = dict(zip(headers, sequences))

#default ORF length is 50bp. Ask user for ORF length, if user provides more than 50 use that value else use 50
ORF_length=50
user_ORF_len=int(input('Enter the minimum ORF length: '))
if user_ORF_len>ORF_length:
    ORF_length=user_ORF_len
    
def codon15(x):
    codon = ' '.join(x[i:i+3] for i in range(0,len(x),3))
    a = 0
    b = 59
    for line in codon:
        splitcodon = ""
        if (len(splitcodon) < 60):
           break 
        else:
            
            splitcodon = codon[a:b]
            print(splitcodon)
            a = a + 60
            b = b + 60
        
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
            fw_frame = match1.group(0)
            print(seq_name[0]+" | FRAME= "+str(frame1)+" | POS= "+ str(pos1)+" | LEN= "+str(length1)+ "\n"+str(codon15(fw_frame)))
    
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
            rev_frame = match2.group(0)
            print(seq_name[0]+" | FRAME= "+str(frame2)+" | POS= "+ str(pos2)+" | LEN= "+str(length2)+"\n"+str(codon15(rev_frame)))

    
    
