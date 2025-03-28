import unittest
from typing import List

from ._1732_Find_the_Highest_Altitude import Solution


class SolutionTest(unittest.TestCase):

    def run_test(self, gain: List[int], result: int):
        self.assertEqual(result, Solution().largestAltitude(gain))

    def test_case_1(self):
        self.run_test([-5, 1, 5, 0, -7], 1)

    def test_case_2(self):
        self.run_test([-4, -3, -2, -1, 4, 3, 2], 0)


if __name__ == "__main__":
    unittest.main()
