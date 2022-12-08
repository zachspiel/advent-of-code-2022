import unittest
from day07 import main


class TestDay7(unittest.TestCase):
    def runTest(self):
        partAResult, partBResult = main()
        self.assertEqual(partAResult, 1423358.0)
        self.assertEqual(partBResult, 545729.0)


unittest.main()
