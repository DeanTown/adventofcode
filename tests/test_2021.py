import unittest

from y2021 import day1, day2, day3


class Test2021(unittest.TestCase):
    # @unittest.skip("Skip!")
    def test_day1(self):
        results = day1.go()
        self.assertEqual(results[0], 1791)
        self.assertEqual(results[1], 1822)

    # @unittest.skip("Skip!")
    def test_day2(self):
        results = day2.go()
        self.assertEqual(results[0], 2039256)
        self.assertEqual(results[1], 1856459736)

    # @unittest.skip("Skip!")
    def test_day3(self):
        results = day3.go()
        self.assertEqual(results[0], 2967914)
        self.assertEqual(results[1], 7041258)
