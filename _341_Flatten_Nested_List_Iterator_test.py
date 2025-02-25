import unittest

from _341_Flatten_Nested_List_Iterator import NestedIterator


class SolutionTest(unittest.TestCase):
    def run_test(self, nestedList, result):
        i, v = NestedIterator(nestedList), []

        while i.hasNext():
            v.append(i.next())

        self.assertEqual(v, result)

    def test_case_1(self):
        self.run_test([[1, 1], 2, [1, 1]], [1, 1, 2, 1, 1])

    def test_case_2(self):
        self.run_test([1, [4, [6]]], [1, 4, 6])

    def test_case_3(self):
        self.run_test([1, 2, 3], [1, 2, 3])


if __name__ == "__main__":
    unittest.main()

