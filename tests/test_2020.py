import unittest

from y2020 import day4


class Test2021(unittest.TestCase):
    # @unittest.skip("Skip!")
    def test_day4(self):
        results = day4.go()
        self.assertEqual(results[0], 256)
        self.assertEqual(results[1])
