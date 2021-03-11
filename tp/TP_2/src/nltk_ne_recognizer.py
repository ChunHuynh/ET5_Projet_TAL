import sys

from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk import ne_chunk

inputPath = sys.argv[1] 	# wsj_0010_sample.txt
outputPath = sys.argv[2]	# wsj_0010_sample.txt.ne.nltk

inputFile = open(inputPath, "r+")
outputFile = open(outputPath, "w")

for line in inputFile:
	tokenizedText = word_tokenize(line)
	tokensTagged = pos_tag(tokenizedText)
	namedEnt = ne_chunk(tokensTagged, binary=False)

	for tokenNe in namedEnt:
		if type(tokenNe).__name__ == "Tree":
			outputFile.write(str(tokenNe) + "\n")

inputFile.close()
outputFile.close()