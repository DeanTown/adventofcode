import unittest

from y2022 import day1, day2, day3, day4, day5, day6, day7, day8

class Test2022(unittest.TestCase):

    def test_day1(self):
        results = day1.go()
        self.assertEqual(results[0], 68923)
        self.assertEqual(results[1], 200044)

    def test_day2(self):
        results = day2.go()
        self.assertEqual(results[0], 13005)
        self.assertEqual(results[1], 11373)

    def test_day3(self):
        results = day3.go()
        self.assertEqual(results[0], 7727)
        self.assertEqual(results[1], 2609)

    def test_day4(self):
        results = day4.go()
        self.assertEqual(results[0], 487)
        self.assertEqual(results[1], 849)

    def test_day5(self):
        results = day5.go()
        self.assertEqual(results[0], 'BZLVHBWQF')
        self.assertEqual(results[1], 'TDGJQTZSL')

    def test_day6(self):
        results = day6.go()
        self.assertEqual(results[0], 1356)
        self.assertEqual(results[1], 2564)

    def test_day7(self):
        results = day7.go()
        self.assertEqual(results[0], 1325919)
        self.assertEqual(results[1], 2050735)

    def test_day8(self):
        results = day8.go()
        self.assertEqual(results[0], 1835)
        self.assertEqual(results[1], False)