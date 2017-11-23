dnaSeq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT" #DNA Sequence which will be Searched through.
findSec = dnaSeq.find("GAATTC") + 1 #Finds the length of the first side of the sequence
Section2 =  len(dnaSeq) - findSec #Finds the length of the other side of the sequence
print("The Length of the first fragment is ",findSec,"and the the length of the second fragment is",Section2,) #Prints the output
