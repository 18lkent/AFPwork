dnaSequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT" #The sequence being counted from
print("This program will display the gc content of a DNA sequence")
seqLen = len(dnaSequence) #Length of the sequence
gAmount = dnaSequence.count('G') #Amount of G's in the sequence
cAmount = dnaSequence.count('C') #Amount of C's in the sequence
seqPer1 = gAmount + cAmount #Adds number of C's and number of G's
seqPer2 = seqPer1/seqLen*100 #Calculates percentage of G's and C's of sequence
print("The GC content of the sequence is {0:.2f}".format(seqPer2)) #The format method allows me to change the amount of decimal places
print(str(round(seqPer2, 2))+"%") #Prints Percentage