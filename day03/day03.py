INPUT_FILE = "day03Input.txt"

def readFile(filePath):
	with open(filePath) as file:
		return file.readlines()

def splitLine(line: str):
	formattedLine = line.replace("\n", "")
	length = int(len(line) / 2)
	return line[:length], line[length:]

def findMatch(line):
	firstHalf, secondHalf = splitLine(line)
	for index in range(len(firstHalf)):
		if(firstHalf[index] in secondHalf):
			return firstHalf[index]
	return ""

def calculatePriority(letter: str):
	ALPHABET = ["a", "b", "c", "d", "e", "f", "g", \
		"h", "i", "j", "k", "l", "m", "n", "o", "p", \
		"q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	index = ALPHABET.index(letter.lower())
	
	if(letter.isupper()):
		return index + 27
	return index + 1

def calculateTotalPriorityIndividually():
	totalPriority = 0
	lines = readFile(INPUT_FILE)
	for line in lines:
		match = findMatch(line)
		if(len(match) > 0):
			totalPriority += calculatePriority(match)
	return totalPriority 

def calculatePriorityInGroups():
	totalPriority = 0
	lines = readFile(INPUT_FILE)
	
	for index in range(0, len(lines), 3):
		currentLine = lines[index]
		characterIndex = 0
		foundMatchingCharacter = False
		while(characterIndex < len(currentLine) and not foundMatchingCharacter):
			letter = currentLine[characterIndex]
			isInNextLine = letter in lines[index + 1]
			isInNextNextLine = letter in lines[index + 2]
			if(isInNextLine and isInNextNextLine):
				totalPriority += calculatePriority(letter)
				foundMatchingCharacter = True 
			characterIndex += 1
	
	return totalPriority

print(calculatePriorityInGroups())
				
		
