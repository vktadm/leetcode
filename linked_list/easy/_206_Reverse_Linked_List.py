class Solution(object):
    def do_array(self, head):
        result = []
        if head is None:
            return result

        current_node = head

        while current_node is not None:
            result.append(current_node.val)
            current_node = current_node.next
        return result

    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        current_node = head
        previous_node = None

        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        return self.do_array(previous_node)
