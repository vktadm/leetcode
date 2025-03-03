# class Solution(object):
#
#     def averageOfLevels(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: List[float]
#         """
#         result = []
#         parents = [root]
#         children = []
#         value = 0
#         counter = 0
#
#         while True:
#             if not parents:
#                 result.append(value / counter)
#                 if not children:
#                     return result
#                 else:
#                     parents = list(children)
#                     children = []
#                     value = 0
#                     counter = 0
#
#             node = parents.pop(0)
#             value += node.val
#             counter += 1
#
#             if node.left:
#                 children.append(node.left)
#             if node.right:
#                 children.append(node.right)


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        result = []
        q = [root]

        while q:
            l = len(q)
            level = []
            for _ in range(l):
                node = q.pop(0)
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if level:
                result.append(float(sum(level)) / float(len(level)))
        return result
