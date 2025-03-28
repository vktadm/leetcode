import unittest
from typing import List

from ._1207_Unique_Number_of_Occurrences import Solution


class SolutionTest(unittest.TestCase):

    def run_test(self, arr: List[int], result: bool):
        self.assertEqual(result, Solution().uniqueOccurrences(arr))

    def test_case_1(self):
        self.run_test([1, 2, 2, 1, 1, 3], True)

    def test_case_2(self):
        self.run_test([1, 2], False)

    def test_case_3(self):
        self.run_test([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True)


if __name__ == "__main__":
    unittest.main()
