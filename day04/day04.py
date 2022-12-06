INPUT_FILE = "day04Input.txt"

def readFile(filePath):
	with open(filePath) as file:
		return file.readlines()

def getRangeFromPair(pair):
	start, end = pair.split("-")
	
	return int(start), int(end)
	
def calculateOverlappingPairs():
	lines = readFile(INPUT_FILE)
	totalOverlappingPairs = 0
	partialOverlappingPairs = 0
	
	for line in lines:
		pairOne, pairTwo = line.split(",")
	
		startOne, endOne = getRangeFromPair(pairOne)
		startTwo, endTwo = getRangeFromPair(pairTwo)
		
		if((startOne <= startTwo and endOne >= endTwo) or (startOne >= startTwo and endOne <= endTwo)):
			totalOverlappingPairs += 1
		
		if(endOne >= startTwo and endTwo >= startOne):
			partialOverlappingPairs += 1
	
	return totalOverlappingPairs, partialOverlappingPairs

print(calculateOverlappingPairs())		
