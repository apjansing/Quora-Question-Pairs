from nltk.corpus import stopwords
import nltk
import re
import pandas as pd

def formatPart(part):
	part = removeSymbols(part)
	part = removeStopWords(part.split(" "))	
	return part.strip()

def removeSymbols(line):
	return re.sub('[^\w]', ' ', line)


def removeStopWords(words):
	line = ""
	for word in words:
		if word not in stopwords.words('english'):
			line = line + " " + word
	return line

def formatRow(entry):
	print entry

def processPart(part, j):
	# if j is 3 or j is 4:
	if j is 1 or j is 2:
		return formatPart(part)
	else:
		return part

def getHeader(noStop):
	with open("train.csv", "r") as F:
		for f in F:
			noStop.write(f)
			break

if __name__ == "__main__":
	header = True
	# trainingSet = pd.read_csv("train.csv", quotechar='"').as_matrix()
	trainingSet = pd.read_csv("test.csv", quotechar='"').as_matrix()
	rows = len(trainingSet[:,0])
	L = []
	# with open("trainNoStopWords.csv", "w") as noStop:
	with open("testNoStopWords.csv", "w") as noStop:
		getHeader(noStop)
		for i in range(rows):
			l = []
			for j in range(len(trainingSet[i,:])):
				l.append(processPart(str(trainingSet[i,j]), j))
			noStop.write(",".join(l) + "\n")