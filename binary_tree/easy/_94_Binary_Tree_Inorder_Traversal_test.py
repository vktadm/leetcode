import unittest

from _94_Binary_Tree_Inorder_Traversal import Solution
from create_tree import create_tree


class SolutionTest(unittest.TestCase):
    def run_test(self, nodes, result):
        root = create_tree(nodes)
        self.assertEqual(result, Solution().inorderTraversal(root))

    def test_case_1(self):
        self.run_test([1, None, 2, 3], [1, 3, 2])

    def test_case_2(self):
        self.run_test([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9], [4, 2, 6, 5, 7, 1, 3, 9, 8])


if __name__ == "__main__":
    unittest.main()
