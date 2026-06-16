from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree(lst: List) -> Optional[TreeNode]:
    """Создаёт бинарное дерево из списка в порядке level-order (BFS)"""
    if not lst or lst[0] is None:
        return None

    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1  # индекс следующего элемента в списке

    while queue and i < len(lst):
        node = queue.popleft()

        # Левый ребёнок
        if i < len(lst):
            if lst[i] is not None:
                node.left = TreeNode(lst[i])
                queue.append(node.left)

            i += 1

        # Правый ребёнок
        if i < len(lst):
            if lst[i] is not None:
                node.right = TreeNode(lst[i])
                queue.append(node.right)

            i += 1

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


def print_tree(root, prefix="", is_left=True):
    if root is None:
        return

    if root.right:
        print_tree(root.right, prefix + ("│   " if is_left else "    "), False)

    print(prefix + ("└── " if is_left else "┌── ") + str(root.val))

    if root.left:
        print_tree(root.left, prefix + ("    " if is_left else "│   "), True)
