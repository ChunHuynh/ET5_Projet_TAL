import sys

inputPath = sys.argv[1]		#sample.ner.txt.output 	sample.ner.txt.format
outputPath = sys.argv[2]	#Sample_NER_en.txt.output 	Sample_NER_en.txt.format

# Read input file
inputFile = open(inputPath,'r+')

# File to write output results
outputFile = open(outputPath, "w+")


n = 0 # Number of named entities
entityByType = {}

for line in inputFile:
	words = line.split(" ")
	for word in words:
		entity = word.split("/")
		
		if (len(entity) == 2):
			if (entity[1] != 'O'):
				if (entity[1] in entityByType):
					# append the new entity to the existing array for this entity type
					entityByType[entity[1]].append(entity[0])
				else:
					# create a new array for this entity type
					entityByType[entity[1]] = [entity[0]]
			
				n += 1

outputFile.write("{:>15} {:>12} {:>12} {:>15}".format("Entity", "Type", "Occurences", "Proportion") + "\n")

for eType in entityByType:
	entities = entityByType[eType]
	for e in list(set(entities)):
		occ = entities.count(e)
		proportion = str(occ) + "/" + str(n)  + " (" + "{0:.2f}".format((occ/n)*100) + "%)"

		outputFile.write('{:>15}  {:>12}  {:>12} {:>15}'.format(e, eType, str(occ), proportion) + '\n')

inputFile.close()
outputFile.close()