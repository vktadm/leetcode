import unittest
from collections import deque
from typing import Optional
from binary_tree.easy.create_tree import TreeNode, create_tree


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))


class TestMinDepth(unittest.TestCase):

    def test_example1(self):
        """Example 1: Balanced tree with min depth 2"""
        root = create_tree([3, 9, 20, None, None, 15, 7])
        self.assertEqual(Solution().minDepth(root), 2)

    def test_example2(self):
        """Example 2: Right-skewed tree with min depth 5"""
        root = create_tree([2, None, 3, None, 4, None, 5, None, 6])
        self.assertEqual(Solution().minDepth(root), 5)

    def test_single_node(self):
        """Edge case: Tree with only root"""
        root = create_tree([1])
        self.assertEqual(Solution().minDepth(root), 1)

    def test_empty_tree(self):
        """Edge case: Empty tree"""
        root = create_tree([])
        self.assertEqual(Solution().minDepth(root), 0)

    def test_left_only_tree(self):
        """Left-skewed tree"""
        root = create_tree([1, 2, None, 3, None, 4])
        self.assertEqual(Solution().minDepth(root), 4)

    def test_right_only_tree(self):
        """Right-skewed tree (different from example)"""
        root = create_tree([1, None, 2, None, 3, None, 4])
        self.assertEqual(Solution().minDepth(root), 4)

    def test_perfect_tree(self):
        """Perfect binary tree of height 3"""
        root = create_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(Solution().minDepth(root), 3)

    def test_unbalanced_tree(self):
        """Unbalanced tree where left side is deeper"""
        root = create_tree([1, 2, 3, 4, None, None, 5])
        self.assertEqual(Solution().minDepth(root), 3)  # via right child

    def test_all_null_children(self):
        """Node with both children null (leaf)"""
        root = create_tree([10, None, None])
        self.assertEqual(Solution().minDepth(root), 1)


if __name__ == "__main__":
    unittest.main()
