from typing import Optional

from binary_tree.easy.create_tree import TreeNode


class Solution:
    def helper(self, root: TreeNode):
        if root is None:
            return []
        leaves = self.helper(root.left) + self.helper(root.right)
        return leaves or [root.val]

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.helper(root1) == self.helper(root2)
