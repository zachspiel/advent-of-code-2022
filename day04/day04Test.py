import unittest
from day04 import calculateOverlappingPairs


class TestDay4(unittest.TestCase):
    def runTest(self):
        partA, partB = calculateOverlappingPairs()
        self.assertEqual(partA, 475)
        self.assertEqual(partB, 825)


unittest.main()
