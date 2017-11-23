dnaSeq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT" #The sequence being modified
dnaSeq1 = dnaSeq.replace("A", "t").replace("G","c")
dnaComp1 = dnaSeq1.replace("T","a").replace("C","g")
newSeq = dnaComp1.upper()
print("Original Sequence:\n"+dnaSeq)
print("Complemntary DNA Sequence:\n"+newSeq)
