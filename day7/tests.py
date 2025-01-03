import unittest

from common.common import read_input_lines
from impl import part1, part2


class AdventOfCodeTests(unittest.TestCase):

    def test_part1_sample(self):
        self.assertEqual(3749, part1(read_input_lines("sample.txt")))

    def test_part1_input(self):
        self.assertEqual(4998764814652, part1(read_input_lines("input.txt")))

    def test_part2_sample(self):
        self.assertEqual(11387, part2(read_input_lines("sample.txt")))

    def test_part2_input(self):
        # 34203806308266 is too low
        self.assertEqual(37598910447546, part2(read_input_lines("input.txt")))


if __name__ == '__main__':
    unittest.main()
