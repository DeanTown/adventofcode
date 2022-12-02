import unittest

from y2022 import day1, day2

class Test2022(unittest.TestCase):

    def test_day1(self):
        results = day1.go()
        self.assertEqual(results[0], 68923)
        self.assertEqual(results[1], 200044)

    def test_day2(self):
        results = day2.go()
        self.assertEqual(results[0], 13005)
        self.assertEqual(results[1], 11373)