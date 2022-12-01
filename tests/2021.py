import unittest

from y2021 import day1

class Test2021(unittest.TestCase):

    def test_day1(self):
        results = day1.go()
        self.assertEqual(results[0], 1791)
        self.assertEqual(results[1], 1822)