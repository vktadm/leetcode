import unittest

from _222_Count_Complete_Tree_Nodes import Solution
from create_tree import create_tree


class SolutionTest(unittest.TestCase):
    def run_test(self, lst, result):
        root = create_tree(lst)
        self.assertEqual(result, Solution().countNodes(root))

    def test_case_1(self):
        self.run_test([1, 2, 3, 4, 5, 6], 6)

    def test_case_2(self):
        self.run_test([], 0)

    def test_case_3(self):
        self.run_test([1], 1)


if __name__ == "__main__":
    unittest.main()
