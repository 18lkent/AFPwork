progType = input("Would you like to Encode or Decode Text? ").upper()
if progType == "ENCODE":
    encodeText = input("Enter text to encode: ").upper()
    Encode = encodeText.replace("A", "f44").replace("B", "a4").replace("C", "a14").replace("D", "e34").replace("E","b64").replace("F", "d14").replace("G", "c44").replace("H", "b54").replace("I", "c24").replace("J", "d34").replace("K", "f34").replace("L", "e64").replace("M", "a24").replace("N", 'd54').replace("O", "b34").replace("P", "a64").replace("Q","d64").replace("R", "b14").replace("S", "d24").replace("T", "b44").replace("U", "a54").replace("V", "b24").replace("W","a34").replace("X", "f54").replace("Y", "c64").replace("Z", "c1F")
    Encode = Encode.upper()
    print(Encode)