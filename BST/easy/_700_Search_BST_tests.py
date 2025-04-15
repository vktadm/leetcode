import unittest
from typing import List

from _700_Search_BST import Solution
from binary_tree.easy.create_tree import create_tree


class SolutionTest(unittest.TestCase):
    def run_test(self, lst: List[int | None], result: bool):
        root = create_tree(lst)
        self.assertEqual(result, Solution().searchBST(root))

    def test_case_1(self):
        self.run_test([4, 2, 7, 1, 3], 2)

    def test_case_2(self):
        self.run_test([4, 2, 7, 1, 3], 5)


if __name__ == "__main__":
    unittest.main()
