import re
INPUT_FILE = "day05Input.txt"


def readFile(filePath):
    with open(filePath) as file:
        return file.readlines()


def createInitialStacks(lines):
    index = 0
    stacks = []

    while("[" in lines[index]):
        line = lines[index]
        stackIndex = 0
        for innerIndex in range(1, len(line), 4):

            if(stackIndex >= len(stacks)):
                stacks.append([])

            if(line[innerIndex] != " "):
                stacks[stackIndex].insert(0, line[innerIndex])
            stackIndex += 1
        index += 1

    return stacks


def findInstructionsIndex(lines):
    return lines.index("\n") + 1


def getInstructions(line):
    temp = re.findall(r'\d+', line)
    totalToMove, stackToPop, stackToPush = list(map(int, temp))

    return totalToMove, stackToPop - 1, stackToPush - 1


def getLettersOnTop(stacks):
    lettersOnTop = map(lambda x: x[len(x) - 1], stacks)
    return "".join(list(lettersOnTop))


def moveCrates():
    lines = readFile(INPUT_FILE)
    stacks = createInitialStacks(lines)

    for index in range(findInstructionsIndex(lines), len(lines)):
        totalToMove, source, destination = getInstructions(lines[index])
        stacks[destination] += getPoppedItems(stacks, source, totalToMove)
        stacks[source] = stacks[source][:len(stacks[source]) - totalToMove]

    return getLettersOnTop(stacks)


def getPoppedItems(stacks, source, totalToMove):
    poppedItems = stacks[source][len(stacks[source]) - totalToMove:]
    poppedItems.reverse()
    return poppedItems


def moveCratesInOriginalOrder():
    lines = readFile(INPUT_FILE)
    stacks = createInitialStacks(lines)
    for index in range(findInstructionsIndex(lines), len(lines)):
        totalToMove, source, destination = getInstructions(lines[index])

        itemsToAdd = stacks[source][len(stacks[source]) - totalToMove:]
        stacks[destination] += itemsToAdd
        stacks[source] = stacks[source][:len(stacks[source]) - totalToMove]

    return getLettersOnTop(stacks)
