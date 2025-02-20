class Solution(object):

    def array(self, root):
        if not root or not (root.left or root.right):
            return True

        children = [root.left, root.right]

        while children:
            left_branch = children.pop(0)
            right_branch = children.pop(0)

            if left_branch is None and right_branch is None:
                continue
            elif left_branch and right_branch and left_branch.val == right_branch.val:
                children.append(left_branch.left)
                children.append(right_branch.right)

                children.append(left_branch.right)
                children.append(right_branch.left)
            else:
                return False

        return True

    def recursion(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val == q.val:
            return self.recursion(p.left, q.right) and self.recursion(p.right, q.left)
        else:
            return False

    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # array_solve = self.array(root)

        if not root:
            return True
        return self.recursion(root.left, root.right)
