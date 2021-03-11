import sys

from nltk import pos_tag
from nltk import RegexpParser
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
  
lemmatizer = WordNetLemmatizer() 

inputPath = sys.argv[1] 	# wsj_0010_sample.txt
outputPath = sys.argv[2]	# wsj_0010_sample.txt.chk.nltk

patternsFile = open(sys.argv[3], "r+")
inputFile = open(inputPath, "r+")
outputFile = open(outputPath, 'w')

tokenizedText = word_tokenize(inputFile.read())

tokensTagged = pos_tag(tokenizedText)

for pattern in patternsFile:
    outputFile.write(pattern)

    chunker = RegexpParser(pattern)

    output = chunker.parse(tokensTagged)
    outputSplit = str(output).split("\n")
    for chunk in outputSplit:
        if ("Compound" in chunk):
            outputFile.write(chunk.replace("Compound ", "") + "\n")
    
    outputFile.write("\n")

patternsFile.close()
inputFile.close()
outputFile.close()