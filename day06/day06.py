INPUT_FILE = "day06Input.txt"


def readFile(filePath):
    with open(filePath) as file:
        return file.readlines()


def findStartOfPacketMarkers():
    lines = readFile(INPUT_FILE)
    partA = findMarkerIndex(lines[0], 4)
    partB = findMarkerIndex(lines[0], 14)
    return partA, partB


def findMarkerIndex(line, packetSize):
    characters = list(line.replace("\n", ""))
    index = 0
    while(index < len(characters)):
        currentSet = characters[index:index + packetSize]
        if(len(set(currentSet)) == packetSize):
            return index + packetSize
        index += 1

    return -1
