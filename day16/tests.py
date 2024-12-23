import unittest

from common.common import read_input_lines
from impl import part1, part2


class AdventOfCodeTests(unittest.TestCase):

    def test_part1_sample(self):
        self.assertEqual(7036, part1(read_input_lines("sample.txt")))

    def test_part1_input(self):
        # 123492 is too high
        # 123492 is too high
        self.assertEqual(122492, part1(read_input_lines("input.txt")))

    def test_part2_sample(self):
        self.assertEqual(45, part2(read_input_lines("sample.txt")))

    def test_part2_sample2(self):
        self.assertEqual(64, part2(read_input_lines("sample2.txt")))

    def test_part2_input(self):
        self.assertEqual(520, part2(read_input_lines("input.txt")))


if __name__ == '__main__':
    unittest.main()
