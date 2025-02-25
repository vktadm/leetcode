import unittest

from intervals.medium._56_Merge_Intervals import Solution


class SolutionTest(unittest.TestCase):
    def run_test(self, intervals, result):
        self.assertEqual(Solution().merge(intervals), result)

    def test_case_1(self):
        self.run_test([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]])

    def test_case_2(self):
        self.run_test([[1, 4], [4, 5]], [[1, 5]])

    def test_case_3(self):
        self.run_test([], [])

    def test_case_5(self):
        self.run_test([[1, 2]], [[1, 2]])

    def test_case_6(self):
        self.run_test([[1, 3], [2, 6], [6, 10], [15, 18]], [[1, 10], [15, 18]])

    def test_case_7(self):
        self.run_test([[1, 4], [0, 4]], [[0, 4]])

    def test_case_8(self):
        self.run_test([[1, 4], [1, 4]], [[1, 4]])

    def test_case_9(self):
        self.run_test([[1, 4], [0, 2], [3, 5]], [[0, 5]])

    def test_case_10(self):
        self.run_test([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]], [[1, 10]])


if __name__ == "__main__":
    unittest.main()
