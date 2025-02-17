import unittest
from collections import deque

from _100_Same_Tree import Solution, TreeNode


class SolutionTest(unittest.TestCase):
    def run_test(self, result, root1, root2):
        s = Solution()
        self.assertEqual(result, s.isSameTree(root1, root2))

    def test_case_1(self):
        nodes1 = [1, 2, 3]
        nodes2 = [1, 2, 3]

        root1 = TreeNode(1, TreeNode(2), TreeNode(3))
        root2 = TreeNode(1, TreeNode(2), TreeNode(3))

        self.run_test(True, root1, root2)

    def test_case_2(self):
        nodes1 = [1, None, 3, 4, 5]
        nodes2 = [1, 3, None, 4, 5]

        root1 = TreeNode(1, None, TreeNode(3))
        root1.right.left = TreeNode(4)
        root1.right.right = TreeNode(5)

        root2 = TreeNode(1, TreeNode(3), None)
        root2.left.left = TreeNode(4)
        root2.left.right = TreeNode(5)

        self.run_test(False, root1, root2)

    def test_case_3(self):
        nodes1 = [1]
        root1 = TreeNode(1)

        nodes2 = [1]
        root2 = TreeNode(1)

        self.run_test(True, root1, root2)


if __name__ == "__main__":
    unittest.main()
