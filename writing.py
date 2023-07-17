# printing contents of a file
# open files
seq_1file = open("seq1.txt")
seq_2file = open("seq2.txt")

# read files
seq_1cont = seq_1file.read()
seq_2cont = seq_2file.read()

#print contents of files
print(seq_1cont)
print(seq_2cont)

seq_com = seq_1cont + seq_2cont

print(seq_com)