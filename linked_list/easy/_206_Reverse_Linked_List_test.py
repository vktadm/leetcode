import unittest

from _206_Reverse_Linked_List import Solution
from linked_list import Arr


class SolutionTest(unittest.TestCase):

    def run_test(self, lst, result):
        lst_node = Arr(lst)

        self.assertEqual(Solution().reverseList(lst_node.head), result)

    def test_case_1(self):
        self.run_test([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])

    def test_case_2(self):
        self.run_test([1, 2], [2, 1])

    def test_case_3(self):
        self.run_test([], [])


if __name__ == "__main__":
    unittest.main()
