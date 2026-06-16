import unittest
from typing import Optional
from binary_tree.easy.create_tree import TreeNode, create_tree


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            if left == -1:
                return -1

            right = dfs(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return dfs(root) != -1


class TestBalancedBinaryTree(unittest.TestCase):
    def test_example1(self):
        root = create_tree([3, 9, 20, None, None, 15, 7])
        self.assertTrue(Solution().isBalanced(root))

    def test_example2(self):
        root = create_tree([1, 2, 2, 3, 3, None, None, 4, 4])
        self.assertFalse(Solution().isBalanced(root))

    def test_example3(self):
        root = create_tree([])
        self.assertTrue(Solution().isBalanced(root))

    def test_single_node(self):
        root = create_tree([1])
        self.assertTrue(Solution().isBalanced(root))

    def test_left_skewed(self):
        root = create_tree([1, 2, None, 3])
        self.assertFalse(Solution().isBalanced(root))

    def test_right_skewed(self):
        root = create_tree([1, None, 2, None, 3])
        self.assertFalse(Solution().isBalanced(root))

    def test_perfect_tree(self):
        root = create_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertTrue(Solution().isBalanced(root))

    def test_unbalanced_at_root(self):
        root = create_tree([1, 2, 3, 4, None, None, None, 5])
        self.assertFalse(Solution().isBalanced(root))


if __name__ == "__main__":
    unittest.main()
