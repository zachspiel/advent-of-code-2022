import unittest
from day06 import findStartOfPacketMarkers


class TestDay6(unittest.TestCase):
    def runTest(self):
        partAResult, partBResult = findStartOfPacketMarkers()
        self.assertEqual(partAResult, 1760)
        self.assertEqual(partBResult, 2974)


unittest.main()
