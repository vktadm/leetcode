import unittest

from _435_Non_overlapping_Intervals import Solution


class SolutionTest(unittest.TestCase):
    def run_test(self, intervals, result):
        self.assertEqual(result, Solution().eraseOverlapIntervals(intervals))

    def test_case_1(self):
        self.run_test([[1, 2], [2, 3], [3, 4], [1, 3]], 1)

    def test_case_2(self):
        self.run_test([[1, 2], [1, 2], [1, 2]], 2)

    def test_case_3(self):
        self.run_test([[1, 2], [2, 3]], 0)

    def test_case_4(self):
        self.run_test([[1, 100], [11, 22], [1, 11], [2, 12]], 2)


if __name__ == "__main__":
    unittest.main()
