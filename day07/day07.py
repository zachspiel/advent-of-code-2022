from dataclasses import dataclass, field
import json
from typing import List

INPUT_FILE = "day07Input.txt"
TOTAL_SPACE = 70000000
SPACE_NEEDED = 30000000


@dataclass
class Node:
    name: str
    size: int = 0
    isFile: bool = False
    parent: "Node" = None
    children: dict[str, "Node"] = field(default_factory=dict)

    def toString(self):
        print("Name: ", self.name)
        print("size: ", self.size)
        print("isFile: ", self.isFile)

        if(self.parent is not None):
            print("parent: ", self.parent.name)
        print("children: ", self.children.keys())


def readFile(filePath):
    with open(filePath) as file:
        return file.readlines()


def isChangeDirCommand(line):
    return "$ cd " in line


def isLsCommand(line):
    return "$ ls" in line


def createFileStructure(lines):
    root: Node = Node("/")
    current = root

    for line in lines:
        tokens = line.replace("\n", "").split(" ")
        if(isChangeDirCommand(line)):
            newDir = tokens[2]
            if(newDir == "/"):
                current = root
            elif(newDir == ".."):
                current = current.parent
            else:
                if(newDir not in current.children.keys()):
                    current.children[newDir] = Node(newDir)
                current = current.children[newDir]
        elif(not isLsCommand(line)):
            isFile = "dir" not in line
            size, name = tokens

            if(name not in current.children.keys()):
                current.children[name] = Node(
                    name=name, size=getSize(size), isFile=isFile, parent=current)
    return root


def getSize(size):
    try:
        return float(size)
    except:
        return 0


def calculateSum(node: Node, sizes: List[int]):
    if(node.isFile):
        return node.size, sizes

    childSum = 0
    for child in node.children.values():
        childSum += calculateSum(child, sizes)[0]
    sizes.append(childSum)
    return sizes[-1], sizes


def sumSmallestDirectories(sizes: List[int]):
    return sum(filter(lambda x: x < 100000, sizes))


def findDirectoryToRemove(totalUsedSpace: float, sizes: list[int]):
    unusedSpace = TOTAL_SPACE - totalUsedSpace
    directoriesToDelete = filter(
        lambda x: unusedSpace + x >= SPACE_NEEDED, sizes)

    return min(list(directoriesToDelete))


def main():
    lines = readFile(INPUT_FILE)
    fileStructure = createFileStructure(lines)
    current, sizes = calculateSum(fileStructure, [])
    partA = sumSmallestDirectories(sizes)
    partB = findDirectoryToRemove(current, sizes)
    return partA, partB
