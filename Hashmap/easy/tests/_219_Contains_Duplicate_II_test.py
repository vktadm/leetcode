import unittest

from Hashmap.easy._219_Contains_Duplicate_II import Solution


class SolutionTest(unittest.TestCase):

    def run_test(self, result, nums, k):
        self.assertEqual(result, Solution().containsNearbyDuplicate(nums, k))

    def test_case_1(self):
        self.run_test(True, [1, 2, 3, 1], 3)

    def test_case_2(self):
        self.run_test(True, [1, 0, 1, 1], 1)

    def test_case_3(self):
        self.run_test(False, [1, 2, 3, 1, 2, 3], 2)


if __name__ == "__main__":
    unittest.main()
