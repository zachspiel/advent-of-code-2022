INPUT_FILE = "day06Input.txt"

def readFile(filePath):
	with open(filePath) as file:
		return file.readlines()

def findAllMarkers():
	lines = readFile(INPUT_FILE)
	
	for line in lines:
		print(findMarkerIndex(line, 4))
		print(findMarkerIndex(line, 14))
		
def findMarkerIndex(line, packetSize):
	characters = list(line.replace("\n", ""))
	index = 0
	while(index < len(characters)):
		currentSet = characters[index:index + packetSize]
		if(len(set(currentSet)) == len(currentSet)):
			return index + packetSize
		index += 1
	
	return -1
	
	
findAllMarkers()
	
