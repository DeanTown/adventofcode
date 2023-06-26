import unittest

import y2021


class Test2021(unittest.TestCase):
    def test_day1(self):
        results = y2021.day1.go()
        self.assertEqual(results[0], 1791)
        self.assertEqual(results[1], 1822)

    def test_day2(self):
        results = y2021.day2.go()
        self.assertEqual(results[0], 2039256)
        self.assertEqual(results[1], 1856459736)
