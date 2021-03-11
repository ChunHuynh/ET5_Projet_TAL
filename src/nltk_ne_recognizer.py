import sys

from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk import ne_chunk

inputPath = sys.argv[1]
outputPath = sys.argv[2]

inputFile = open(inputPath, "r+")
outputFile = open(outputPath, 'w')

for line in inputFile:
    tokenizedText = word_tokenize(line)
    tokensTagged = pos_tag(tokenizedText)
    namedEnt = ne_chunk(tokensTagged, binary=False)
    #print(namedEnt)
    for tokenNe in namedEnt:
        if type(tokenNe).__name__ == "Tree":
            lb = tokenNe.label()

            for leaf in tokenNe.leaves():
                if lb == "ORGANIZATION":
                    outputFile.write(leaf[0] + "\t" + "ORGANIZATION" + "\n")
                elif lb == "PERSON":
                    outputFile.write(leaf[0] + "\t" + "PERSON" + "\n")
                elif lb == "GPE" or lb == "FACILITY" or lb == "GSP":
                    outputFile.write(leaf[0] + "\t" + "LOCATION" + "\n")
        else:
            outputFile.write(tokenNe[0] + "\t" + "O" + "\n")

inputFile.close()
outputFile.close()