import unittest

import y2022


class Test2022(unittest.TestCase):
    def test_day1(self):
        results = y2022.day1.go()
        self.assertEqual(results[0], 68923)
        self.assertEqual(results[1], 200044)

    def test_day2(self):
        results = y2022.day2.go()
        self.assertEqual(results[0], 13005)
        self.assertEqual(results[1], 11373)

    def test_day3(self):
        results = y2022.day3.go()
        self.assertEqual(results[0], 7727)
        self.assertEqual(results[1], 2609)

    def test_day4(self):
        results = y2022.day4.go()
        self.assertEqual(results[0], 487)
        self.assertEqual(results[1], 849)

    def test_day5(self):
        results = y2022.day5.go()
        self.assertEqual(results[0], "BZLVHBWQF")
        self.assertEqual(results[1], "TDGJQTZSL")

    def test_day6(self):
        results = y2022.day6.go()
        self.assertEqual(results[0], 1356)
        self.assertEqual(results[1], 2564)

    def test_day7(self):
        results = y2022.day7.go()
        self.assertEqual(results[0], 1325919)
        self.assertEqual(results[1], 2050735)

    def test_day8(self):
        results = y2022.day8.go()
        self.assertEqual(results[0], 1835)
        self.assertEqual(results[1], 263670)

    # def test_day9(self):
    #     results = y2022.day9.go()
    #     self.assertEqual(results[0], False)
    #     self.assertEqual(results[1], False)

    def test_day10(self):
        results = y2022.day10.go()
        self.assertEqual(results[0], 14360)
        self.assertEqual(
            results[1],
            "###...##..#..#..##..####.###..####.####.#..#.#..#.#.#..#..#.#....#..#.#.......#.###..#....##...#..#.###..#..#.###....#..#..#.#.##.#.#..####.#....###..#.....#...#..#.#..#.#.#..#..#.#....#.#..#....#....###...###.#..#.#..#.####.#..#.####.####.",
        )

    def test_day11(self):
        results = y2022.day11.go()
        self.assertEqual(results[0], 151312)
        self.assertEqual(results[1], False)
