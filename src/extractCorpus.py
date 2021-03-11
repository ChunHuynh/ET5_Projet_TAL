import sys

#python3.8 src/extractCorpus.py data/pos_reference.txt.lima data/pos_test.txt
inputPath = sys.argv[1]
outputPath = sys.argv[2]

inputFile  = open(inputPath, 'r')
outputFile = open(outputPath, "w+")

for line in inputFile:
	if line == "\n":
		outputFile.write("\n")
	else:
		arrLine = line.split()
		key = arrLine[0]
		outputFile.write(key + " ")

inputFile.close()
outputFile.close()