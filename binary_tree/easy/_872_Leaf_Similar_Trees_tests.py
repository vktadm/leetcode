import unittest
from typing import List

from _872_Leaf_Similar_Trees import Solution
from create_tree import create_tree


class SolutionTest(unittest.TestCase):
    def run_test(self, lst1: List[int | None], lst2: List[int | None], result: bool):
        root1 = create_tree(lst1)
        root2 = create_tree(lst2)
        self.assertEqual(result, Solution().leafSimilar(root1, root2))

    def test_case_1(self):
        self.run_test(
            [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4],
            [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8],
            True,
        )

    def test_case_2(self):
        self.run_test(
            [1, 2, 3],
            [1, 3, 2],
            False,
        )


if __name__ == "__main__":
    unittest.main()
