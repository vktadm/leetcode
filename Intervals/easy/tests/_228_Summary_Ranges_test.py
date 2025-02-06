import unittest

from Intervals.easy._228_Summary_Ranges import Solution


class SolutionTest(unittest.TestCase):

    def run_test(self, result, nums):
        self.assertEqual(result, Solution().summaryRanges(nums))

    def test_case_1(self):
        self.run_test(["0->2", "4->5", "7"], [0, 1, 2, 4, 5, 7])

    def test_case_2(self):
        self.run_test(["0", "2->4", "6", "8->9"], [0, 2, 3, 4, 6, 8, 9])


if __name__ == "__main__":
    unittest.main()
