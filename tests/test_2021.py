import unittest

from y2021 import day1, day2, day3, day13, day14


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

    # @unittest.skip("Skip!")
    def test_day13(self):
        results = day13.go()
        self.assertEqual(results[0], 790)
        self.assertEqual(
            results[1],
            "###...##..#..#.####.###..####...##..##.\n#..#.#..#.#..#....#.#..#.#.......#.#..#\n#..#.#....####...#..###..###.....#.#...\n###..#.##.#..#..#...#..#.#.......#.#...\n#....#..#.#..#.#....#..#.#....#..#.#..#\n#.....###.#..#.####.###..#.....##...##.\n\n",
        )

    # @unittest.skip("Skip!")
    def test_day14(self):
        results = day14.go()
        self.assertEqual(results[0], 3411)
        self.assertEqual(results[1], 1111111111111111111)
