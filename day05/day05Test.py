import unittest
from day05 import moveCrates, moveCratesInOriginalOrder


class TestDay5(unittest.TestCase):
    def runTest(self):
        self.assertEqual(moveCrates(), "QNHWJVJZW")
        self.assertEqual(moveCratesInOriginalOrder(), "BPCZJLFJW")


unittest.main()
