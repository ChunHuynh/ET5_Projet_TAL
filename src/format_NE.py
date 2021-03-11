import sys

path = sys.argv[1]
pathOut = sys.argv[2]

file = open(path,'r+')
fileOut = open(pathOut, 'w')

word = ""
NE = ""

for line in file:
	wordWithNE = line.split(" ")
    
	for word in wordWithNE:
		wordAndNE = word.split("/")
		if (len(wordAndNE) >= 2):
			word = wordAndNE[0]
			NE = wordAndNE[1]
			fileOut.write(word + '\t' + NE + '\n')
	
file.close()
fileOut.close()