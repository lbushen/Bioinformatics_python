# A2 solutions

# Q1

# a)Define an array that contains the amino acids in the right order
# (use the three letters notation, as above). Print it in one line.
print("Q1")
print("---------------------------------------")
polypep = ["Phe", "Val", "Asn", "Gln", "His", "Leu", "Cys", "Gly"]
print(polypep)

# b) Determine the number of amino acids in the polypeptide and print it.
polypep_len = len(polypep)
print("Number of aa in polypeptide is " + str(polypep_len) )

# c) Add the amino acid "His" to the end of the polypeptide.
# Print the resulting array in one line.
polypep.append("His")
print(polypep)

# d) Ask the user to enter a number between 1 and the number of
# amino acids in the polypeptide, and print the amino acid in that position
# (e.g. if the user enters "4" the program should print "Gln").

print("Enter a number between 1 and " + str(polypep_len) + " and I will return the aa at that position: ")
num = int(input())
print("The aa at that position is " + polypep[num - 1])

# e)Create an inversion: get two positions in the sequence from the user
# and invert the sequence of the amino acids between them.
# For example, if the user enters 3 and then 6, the program4
# should replace Asn, Gln, His, Leu with Leu, His, Gln, Asn.
# Print the array before and after the inversion.
print ("I will now ask you for 2 position, I will reverse the array at those position")
print ("Enter start of your inversion, a number from 1 to " + str(polypep_len) + ": " )
pos1 = int(input())
print("Enter end of your inversion, starting from " + str(pos1) + " to " + str(polypep_len) + ": " )
pos2 = int(input())
print("Polypep before inversion " + str(polypep) )
# Create sub array for sites of inversion
subArray = polypep[(pos1-1):pos2]
print(subArray)
# Reverse sub array
subArray.reverse()
print(subArray)
# Make new polypeptide with inversion included
polypep = polypep[0:(pos1-1)] + subArray + polypep[pos2:]
print("Polypep after inversion " + str(polypep) )

# Q2
print("Q2")
print("---------------------------------------")
array = ["Trp", "Arg", "Liu", "Ilu", "Asp"]
print("Enter a number from 1 to " + str(len(array)) + ": ")
userNum = int(input())
if userNum < 1 or userNum > len(array):
    print("Error, you did not give me a number from 1 to " + str(len(array)) )
else :
    print("The aa at that position is " + array[userNum - 1])

# Q3
print("Q3")
print("---------------------------------------")
dna = "CCGTAACGC"
# Coverting sting to a list, each character becomes an element in the array
dnaArray = list(dna)
print (dnaArray)
# a)
dnaArray.append('T')
print (dnaArray)
# b)
print("Removing 1st element: " + dnaArray.pop(0) )
print (dnaArray)
# c)
print("Adding T to 1st element")
dnaArray.insert(0, 'T')
print (dnaArray)


