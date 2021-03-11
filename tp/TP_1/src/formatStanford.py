import sys

inputPath = sys.argv[1]   #wsj_0010_sample.pos.ref
outputPath = sys.argv[2]  #wsj_0010_sample.pos.stanford.ref
  
# Read file to be converted
with open(inputPath) as inputFile:
    lines = inputFile.read().splitlines()

# File to write output results
outputFile = open(outputPath, "w")
	
# Format to Stanford POS tagger output format
for line in lines:
	token = line.split()[0]
	tag = "_"+line.split()[1]
	
	outputFile.write(token + tag + " ")
	if token == '.':
		outputFile.write("\n")
		
# Close files
inputFile.close()
outputFile.close()