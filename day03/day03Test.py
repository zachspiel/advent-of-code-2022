import unittest
from day03 import calculatePriorityIndividually, calculatePriorityInGroups


class TestDay3(unittest.TestCase):
    def runTest(self):
        self.assertEqual(calculatePriorityIndividually(), 7727)
        self.assertEqual(calculatePriorityInGroups(), 2609)


unittest.main()
