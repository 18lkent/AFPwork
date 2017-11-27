print("\n")
Seq1 = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
Exons = Seq1[0:63]
Exons2 = Seq1[91:]
introns = Seq1[63:91]
print("The first exon consist of these strands:\n\n"+Exons+"\n\nAnd the second exon cosists of these strands:\n\n"+Exons2,"\n")
exonLengths = len(Exons)+len(Exons2)
finalPercentage = exonLengths/len(Seq1)*100
print("The percentage of Exons in the DNA Sequence is:")
print(str(round(finalPercentage,2))+"%")
print(Exons+introns.lower()+Exons2)
