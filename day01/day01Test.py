import unittest
from day01 import findMaxCalories, findTopThreeCalories, INPUT_FILE, readFile


class TestDay1(unittest.TestCase):
    def runTest(self):
        self.assertTrue(len(readFile(INPUT_FILE)) > 0)
        self.assertEqual(findMaxCalories(), 68442)
        self.assertEqual(findTopThreeCalories(), 204837)


unittest.main()
