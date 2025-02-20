import unittest

from _226_Invert_Binary_Tree import Solution
from create_tree import create_tree


class SolutionTest(unittest.TestCase):
    def run_test(self, nodes, result):
        root = create_tree(nodes)
        self.assertEqual(result, Solution().invertTree(root))

    def test_case_1(self):
        self.run_test([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1])

    def test_case_2(self):
        self.run_test([2, 1, 3], [2, 3, 1])

    def test_case_3(self):
        self.run_test([], [])

    def test_case_4(self):
        self.run_test([1, 2, 3, 4, 5, 6, None, 7, 8, None, 9], [1, 3, 2, None, 6, 5, 4, 9, None, 8, 7])


if __name__ == "__main__":
    unittest.main()
