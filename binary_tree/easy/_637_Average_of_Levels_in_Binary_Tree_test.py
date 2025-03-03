import unittest

from _637_Average_of_Levels_in_Binary_Tree import Solution
from create_tree import create_tree


class SolutionTest(unittest.TestCase):
    def run_test(self, nodes, result):
        root = create_tree(nodes)
        self.assertEqual(result, Solution().averageOfLevels(root))

    def test_case_1(self):
        self.run_test([3, 9, 20, None, None, 15, 7], [3.00000, 14.50000, 11.00000])

    def test_case_2(self):
        self.run_test([3, 9, 20, 15, 7], [3.00000, 14.50000, 11.00000])


if __name__ == "__main__":
    unittest.main()
