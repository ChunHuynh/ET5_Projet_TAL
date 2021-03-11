import sys

# Opening files
inputPath = sys.argv[1]
inputFile = open(inputPath,'r')
outputPath = sys.argv[2]
outputFile = open(outputPath, "w+")

B_PERS = False
B_LOC = False
B_ORG = False

# Conversion
for line in inputFile:
    words = line.split("\t")
    
    entityType = words[1][0:-1]

    if entityType == 'O':
        outputFile.write(words[0] + "\tO\n")
        B_PERS = False
        B_LOC = False
        B_ORG = False
    elif entityType == 'LOCATION':
        if not B_LOC:
            outputFile.write(words[0] + "\tB-LOC\n")
            B_LOC = True
        else:
            outputFile.write(words[0] + "\tI-LOC\n")
        B_PERS = False
        B_ORG = False
    elif entityType == 'PERSON':
        if not B_PERS:
            outputFile.write(words[0] + "\tB-PER\n")
            B_PERS = True
        else:
            outputFile.write(words[0] + "\tI-PER\n")
        B_LOC = False
        B_ORG = False
    elif entityType == 'ORGANIZATION':
        if not B_ORG:
            outputFile.write(words[0] + "\tB-ORG\n")
            B_ORG = True
        else:
            outputFile.write(words[0] + "\tI-ORG\n")
        B_LOC = False
        B_PERS = False
			

inputFile.close()
outputFile.close()