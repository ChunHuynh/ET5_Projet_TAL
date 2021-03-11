import sys
import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize

#nltk.download('averaged_perceptron_tagger')

inputPath = sys.argv[1] 	# wsj_0010_sample.txt
outputPath = sys.argv[2]	# wsj_0010_sample.txt.pos.nltk

inputFile = open(inputPath, "r+")
outputFile = open(outputPath, "w")

for line in inputFile:
	tokenizedText = word_tokenize(line)
	tokensTagged = pos_tag(tokenizedText)

	for token in tokensTagged:
		outputFile.write(token[0] + "_" + token[1] + " ")
		if (token[0] == "."):
			outputFile.write("\n")

inputFile.close()
outputFile.close()