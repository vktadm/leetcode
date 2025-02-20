from create_tree import wide


class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return []

        result = []
        children = [root]

        while children:
            node = children.pop(0)
            node.left, node.right = node.right, node.left

            result.append(node.val)

            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)

        return result
