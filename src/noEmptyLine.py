import sys

# Opening files
inputPath = sys.argv[1]
inputFile = open(inputPath,'r')
outputPath = sys.argv[2]
outputFile = open(outputPath, "w+")

for line in inputFile:
    if line != "\n":
        outputFile.write(line)
			

inputFile.close()
outputFile.close()