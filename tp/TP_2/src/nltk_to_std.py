import sys
import re

inputPath = sys.argv[1]		# wsj_0010_sample.txt.ne.nltk
outputPath = sys.argv[2]	# wsj_0010_sample.txt.std.ne.nltk

inputFile = open(inputPath, "r+")
lines = inputFile.read()#.split("\n")

with open(sys.argv[3]) as std:
	label = std.read().splitlines()
	for lb in label:
		nltk_label = lb.split()[0]
		std_label = lb.split()[1]
		lines = lines.replace(nltk_label, std_label)
std.close()

lines = lines.split("\n")
outputFile = open(outputPath, "w")
for line in lines:
	line = re.sub(r'\/[A-Z]*', "", line) # remove any label
	line = line.replace("(", "") # remove '('
	line = line.replace(")", "") # remove ')'
	field = line.split(" ")
	for i in range(1, len(field)):
		outputFile.write(field[i] + " ")
	outputFile.write(field[0] + "\n")


inputFile.close()
outputFile.close()



