import unittest
from day02 import calculateScoreForPartA, calculateScoreForPartB


class TestDay1(unittest.TestCase):
    def runTest(self):
        self.assertEqual(calculateScoreForPartA(), 13005)
        self.assertEqual(calculateScoreForPartB(), 11373)


unittest.main()
