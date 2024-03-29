import unittest

from y2022 import day1, day2, day3, day4, day5, day6, day7, day8, day9, day10, day11


class Test2022(unittest.TestCase):
    # @unittest.skip("Skip!")
    def test_day1(self):
        results = day1.go()
        self.assertEqual(results[0], 68923)
        self.assertEqual(results[1], 200044)

    # @unittest.skip("Skip!")
    def test_day2(self):
        results = day2.go()
        self.assertEqual(results[0], 13005)
        self.assertEqual(results[1], 11373)

    # @unittest.skip("Skip!")
    def test_day3(self):
        results = day3.go()
        self.assertEqual(results[0], 7727)
        self.assertEqual(results[1], 2609)

    # @unittest.skip("Skip!")
    def test_day4(self):
        results = day4.go()
        self.assertEqual(results[0], 487)
        self.assertEqual(results[1], 849)

    # @unittest.skip("Skip!")
    def test_day5(self):
        results = day5.go()
        self.assertEqual(results[0], "BZLVHBWQF")
        self.assertEqual(results[1], "TDGJQTZSL")

    # @unittest.skip("Skip!")
    def test_day6(self):
        results = day6.go()
        self.assertEqual(results[0], 1356)
        self.assertEqual(results[1], 2564)

    # @unittest.skip("Skip!")
    def test_day7(self):
        results = day7.go()
        self.assertEqual(results[0], 1325919)
        self.assertEqual(results[1], 2050735)

    # @unittest.skip("Skip!")
    def test_day8(self):
        results = day8.go()
        self.assertEqual(results[0], 1835)
        self.assertEqual(results[1], 263670)

    @unittest.skip("Skip!")
    def test_day9(self):
        results = day9.go()
        self.assertEqual(results[0], False)
        self.assertEqual(results[1], False)

    # @unittest.skip("Skip!")
    def test_day10(self):
        results = day10.go()
        self.assertEqual(results[0], 14360)
        self.assertEqual(
            results[1],
            "###...##..#..#..##..####.###..####.####.#..#.#..#.#.#..#..#.#....#..#.#.......#.###..#....##...#..#.###..#..#.###....#..#..#.#.##.#.#..####.#....###..#.....#...#..#.#..#.#.#..#..#.#....#.#..#....#....###...###.#..#.#..#.####.#..#.####.####.",
        )

    # @unittest.skip("Skip!")
    def test_day11(self):
        results = day11.go()
        self.assertEqual(results[0], 151312)
        self.assertEqual(results[1], False)
