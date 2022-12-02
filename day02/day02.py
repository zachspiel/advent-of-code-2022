INPUT_FILE = "day02Input.txt"
ROCK_VALUE = 1
PAPER_VALUE = 2
SCISSORS_VALUE = 3

actions = {
    "rock": {
        "tieValue": ROCK_VALUE,
        "losingValue": SCISSORS_VALUE,
        "winningValue": PAPER_VALUE
    },
    "paper": {
        "tieValue": PAPER_VALUE,
        "losingValue": ROCK_VALUE,
        "winningValue": SCISSORS_VALUE
    },
    "scissors": {
        "tieValue": SCISSORS_VALUE,
        "losingValue": PAPER_VALUE,
        "winningValue": ROCK_VALUE
    }
}


def readFile(path: str):
    with open(path) as file:
        lines = file.readlines()
        return lines


def calculateScoreForPartA():
    lines = readFile(INPUT_FILE)
    score = 0

    for line in lines:
        columns = line.split(" ")
        opponent = columns[0]
        picked = columns[1].replace("\n", "")

        if(wonRound(opponent, picked)):
            score += 6
        elif(isDraw(opponent, picked)):
            score += 3

        score += getScore(picked)

    return score


def wonRound(opponent, picked):
    return opponent == "A" and picked == "Y" or opponent == "B" and picked == "Z" or opponent == "C" and picked == "X"


def isDraw(opponent, picked):
    return convertToCommonString(opponent) == convertToCommonString(picked)


def calculateScoreForPartB():
    lines = readFile(INPUT_FILE)
    score = 0

    for line in lines:
        columns = line.split(" ")
        opponent = columns[0]
        roundType = columns[1].replace("\n", "")

        if(shouldWin(roundType)):
            score += 6
            score += getWinningActionValue(opponent)
        elif(shouldDraw(roundType)):
            score += 3
            score += getDrawActionValue(opponent)
        else:
            score += getLosingActionValue(opponent)

    return score


def shouldWin(roundType):
    return roundType == "Z"


def shouldDraw(roundType):
    return roundType == "Y"


def convertToCommonString(value):
    if(value == "A" or value == "X"):
        return "rock"
    if(value == "B" or value == "Y"):
        return "paper"
    if(value == "C" or value == "Z"):
        return "scissors"


def getWinningActionValue(opponent):
    commonString = convertToCommonString(opponent)
    return actions[commonString]["winningValue"]


def getLosingActionValue(opponent):
    commonString = convertToCommonString(opponent)
    return actions[commonString]["losingValue"]


def getDrawActionValue(opponent):
    commonString = convertToCommonString(opponent)
    return actions[commonString]["tieValue"]


def getScore(picked):
    if(picked == "X"):
        return ROCK_VALUE
    elif(picked == "Y"):
        return PAPER_VALUE
    return SCISSORS_VALUE


print(calculateScoreForPartB())
