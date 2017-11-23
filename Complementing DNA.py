dnaSeq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT" #The sequence being modified
dnaSeq1 = dnaSeq.replace("A", "t").replace("G","c") #Replaces A's with lowercase t's and Uppercase G's with lowercase c's
dnaComp1 = dnaSeq1.replace("T","a").replace("C","g") #Replaces Uppercase T's with lower case A's and Replaces Uppercase C's with lowercase g's
newSeq = dnaComp1.upper() #Converts new sequence to uppercase
print("Original Sequence:\n"+dnaSeq) #prints original sequence
print("Complementary DNA Sequence:\n"+newSeq) #prints New Complementary Sequence
