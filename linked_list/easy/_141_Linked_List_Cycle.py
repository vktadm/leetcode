# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Arr:
    head = None
    node_array = []

    def append_node(self, node):
        if not self.head:
            self.head = ListNode(node)
            self.node_array.append(self.head)
            return

        current_node = self.head

        # Находим последний элемент
        while current_node.next is not None:
            current_node = current_node.next

        new_node = ListNode(node)
        current_node.next = new_node
        self.node_array.append(new_node)

    def print_heads(self):
        current_node = self.head
        while current_node.next is not None:
            print(f'{current_node.val} -> {current_node.next.val}')
            current_node = current_node.next


class Solution(object):

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = set()

        while head:
            if head.next in visited:
                return True

            visited.add(head)
            head = head.next


arr = Arr()
values = [3, 2, 0, -4]

for value in values:
    arr.append_node(value)

arr.print_heads()
arr.node_array[-1].next = arr.node_array[1]
print(arr.node_array[-1].next.val)

s = Solution()
print(s.hasCycle(arr.node_array[0]))
