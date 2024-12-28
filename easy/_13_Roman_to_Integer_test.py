import unittest
from roman import fromRoman

from _13_Roman_to_Integer import Solution


class MajorityTest(unittest.TestCase):

    def library_solve(self, roman_str):
        return fromRoman(roman_str)

    def run_best_time(self, roman_str):
        self.assertEqual(self.library_solve(roman_str), Solution().romanToInt(roman_str))

    def test_case_1(self):
        self.run_best_time("III")

    def test_case_2(self):
        self.run_best_time("LVIII")

    def test_case_3(self):
        self.run_best_time("MCMXCIV")


if __name__ == "__main__":
    unittest.main()
