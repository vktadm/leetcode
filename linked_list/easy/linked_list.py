# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Arr(object):
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
