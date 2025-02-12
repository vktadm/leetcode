# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Arr:
    def __init__(self, lst):
        # Создаем указатель на head
        self.head = None

        # Добавляем эл-ы в связанный список
        for value in lst:
            self.append_node(value)

    def append_node(self, value):
        """Функция, создающая новый элемент связанного списка"""

        # Если первого эл-та еще нет, то создаем
        if self.head is None:
            self.head = ListNode(value)
            return

        current_node = self.head
        # Находим последний элемент
        while current_node.next is not None:
            current_node = current_node.next

        # Добавляем элемент в конец связанного списка
        new_node = ListNode(value)
        current_node.next = new_node


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

    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode(0)
        h1 = list1
        h2 = list2

        previous = head

        while h1 is not None and h2 is not None:
            if h1.val > h2.val:
                previous.next = h2
                h2 = h2.next
            else:
                previous.next = h1
                h1 = h1.next

            previous = previous.next

        if h1 is not None:
            previous.next = h1

        if h2 is not None:
            previous.next = h2

        return self.do_array(head.next)
