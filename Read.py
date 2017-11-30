line = []
file = open("dna_sequence")
file2 = open("trimmed_DNA","w+")
for line in file:
    sequence = line[14:]
    file2.write(sequence)
    print("Processed sequence with length",len(sequence))
