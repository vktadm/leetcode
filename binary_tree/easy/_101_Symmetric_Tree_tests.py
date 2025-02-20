import unittest

from _101_Symmetric_Tree import Solution
from create_tree import create_tree


class SolutionTest(unittest.TestCase):
    def run_test(self, lst, result):
        root = create_tree(lst)
        self.assertEqual(result, Solution().isSymmetric(root))

    def test_case_1(self):
        self.run_test([1, 2, 2, 3, 4, 4, 3], True)

    def test_case_2(self):
        self.run_test([1, 2, 2, None, 3, None, 3], False)

    def test_case_3(self):
        self.run_test([1], True)

    def test_case_4(self):
        self.run_test([], True)

    def test_case_5(self):
        self.run_test([1, 2, 2, 3, 4, 4, 3, 5, 6, None, None, 6], False)

    def test_case_6(self):
        self.run_test([1, 0], False)


if __name__ == "__main__":
    unittest.main()
