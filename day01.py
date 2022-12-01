INPUT_FILE = "day01Input.txt"


def readFile(path: str):
    with open(path) as file:
        lines = file.readlines()
        return lines


def findMaxCalories():
    lines = readFile(INPUT_FILE)
    maxCalories = 0
    currentTotal = 0

    for line in lines:
        if(line == "\n"):
            maxCalories = max(maxCalories, currentTotal)
            currentTotal = 0
        else:
            currentTotal += int(line)

    return maxCalories


def findTopThreeCalories():
    lines = readFile(INPUT_FILE)
    totalCalories = []
    currentTotal = 0

    for line in lines:
        if(line == "\n"):
            totalCalories.append(currentTotal)
            currentTotal = 0
        elif(line == lines[len(lines) - 1]):
            currentTotal += int(line)
            totalCalories.append(currentTotal)
        else:
            currentTotal += int(line)

    totalCalories.sort(reverse=True)
    totalCalories = totalCalories[:3]

    return sum(totalCalories)
