class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree(lst):
    if not lst:
        return None

    root = TreeNode(lst.pop(0))

    children = [root]

    while lst:
        node = children.pop(0)

        if node:
            node.left = TreeNode(lst.pop(0)) if lst[0] else lst.pop(0)
            children.append(node.left)

            if not lst:
                break

            node.right = TreeNode(lst.pop(0)) if lst[0] else lst.pop(0)
            children.append(node.right)

    return root


def wide(root):
    result = []
    children = [root]

    while children:
        node = children.pop(0)
        result.append(node.val)

        if node.left:
            children.append(node.left)
        if node.right:
            children.append(node.right)

    return result
