import sys

"""
Script used to convert a column tag file to line tag
improve use of evaluate.py with line based output
"""

inputPath = sys.argv[1]
outputPath = sys.argv[2]

# Read file to be converted
with open(inputPath) as inputFile:
	lines = inputFile.read().splitlines()

# File to write output results
outputFile = open(outputPath, "w")
	
# Format column to line 
for line in lines:
	if not line.strip():
		# Ignore empty lines
		pass
	else:
		token = line.split()[0]
		tag = "_" + line.split()[1]
		outputFile.write(token + tag + " ")
	if line == ".	.":
		outputFile.write("\n")
	elif token == '.':
		outputFile.write("\n")

# Close files
inputFile.close()
outputFile.close()

