import unittest

from _142_Linked_List_Cycle_II import Solution
from linked_list.linked_list import ListNode


class SolutionTest(unittest.TestCase):

    def test1(self):
        head = ListNode(val=3)
        node1 = ListNode(val=2)
        node2 = ListNode(val=0)
        node3 = ListNode(val=-4)

        head.next = node1
        node1.next = node2
        node2.next = node3
        node3.next = node1

        self.assertEqual(Solution().detectCycle(head), node1)


if __name__ == "__main__":
    unittest.main()
