import sys

#python3.8 src/translateLabel.py data/pos_reference.txt.lima data/pos_reference.txt.ptb data/POSTags_LIMA_PTB_Linux.txt
#python3.8 src/translateLabel.py data/pos_reference.txt.ptb data/pos_reference.txt.univ data/POSTags_PTB_Universal_Linux.txt

# Function to load the equivalences between labels in a dictionary
def loadDict():
    mappingLabel = open(sys.argv[3], 'r')
    labelMap = {}

	# For each equivalence
    for line in mappingLabel:
        arrLine = line.split()
        key = arrLine[0]
        val = arrLine[1]
        labelMap[key] = val

    mappingLabel.close()

    return labelMap

# Opening files
inputPath = sys.argv[1]
inputFile = open(inputPath,'r')
outputPath = sys.argv[2]
outputFile = open(outputPath, "w+")

# Loading the dictionary
labelMap = loadDict()

# Conversion
for line in inputFile:
	if line == "\n":
		outputFile.write("\n")
	words = line.split("\n")
	for word in words:
		wordLabel = word.split("\t")
		if (len(wordLabel) == 2):
			# If the label is already universal, use it as it is
			if (wordLabel[1] in labelMap.values()):
				outputFile.write(wordLabel[0] + "\t" + wordLabel[1] + "\n")
			# Else convert from PTB to universal
			else:
				outputFile.write(wordLabel[0] + "\t" + str(labelMap.get(wordLabel[1])) + "\n")
			

inputFile.close()
outputFile.close()