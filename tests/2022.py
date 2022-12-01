import unittest

from y2022.day1 import go as day1

class Test2022(unittest.TestCase):

    def test_day1(self):
        results = day1.go()
        self.assertEqual(results[0], 68923)
        self.assertEqual(results[1], 200044)