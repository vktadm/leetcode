import unittest
from typing import List

from ._283_Move_Zeroes import Solution


class SolutionTest(unittest.TestCase):

    def run_test(self, nums: List[int], result: List[int]):
        self.assertEqual(result, Solution().moveZeroes(nums))

    def test_case_1(self):
        self.run_test([0, 1, 0, 3, 12], [1, 3, 12, 0, 0])

    def test_case_2(self):
        self.run_test([0], [0])


if __name__ == "__main__":
    unittest.main()
