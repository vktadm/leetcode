import unittest

from _112_Path_Sum import Solution
from create_tree import create_tree


class SolutionTest(unittest.TestCase):
    def run_test(self, lst, targetSum, result):
        root = create_tree(lst)
        self.assertEqual(result, Solution().hasPathSum(root, targetSum))

    def test_case_1(self):
        self.run_test([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True)

    def test_case_2(self):
        self.run_test([1, 2, 3], 5, False)


if __name__ == "__main__":
    unittest.main()
