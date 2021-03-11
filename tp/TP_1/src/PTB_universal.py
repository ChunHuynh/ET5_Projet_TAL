import sys

inputPath = sys.argv[1]   #wsj_0010_sample.txt.pos.stanford			wsj_0010_sample.pos.stanford.ref
outputPath = sys.argv[2]  #wsj_0010_sample.txt.pos.univ.stanford	wsj_0010_sample.txt.pos.univ.ref

# File to write output results
outputFile = open(outputPath, "w")

# Read input file
with open(inputPath) as inputFile:
	outputFile.write(inputFile.read())
	inputFile.close()
	outputFile.close()
	
outputFile = open(outputPath, "r+") # We change mode to allow read & write 
with open(sys.argv[3]) as uni:
	lines = uni.read().splitlines()
	for line in lines:
		# We need to add '_' & ' ' to avoid false matched words
		# Ex: RB and WRB need to be replaced by ADV
		# We can get WADV as a result...
		PTB_label = "_" + line.split()[0] + " "
		uni_label = "_" + line.split()[1] + " "
		
		outputFile.seek(0) # Go back to the beginning of file to reread the file
		file_source = outputFile.read()
		replace_string = file_source.replace(PTB_label, uni_label)
		outputFile.seek(0) # Go back to the beginning of file to erase all content
		outputFile.truncate()
		outputFile.write(replace_string) # Overwrite output with the new output
uni.close()	
outputFile.close()