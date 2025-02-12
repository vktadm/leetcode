import unittest

from _21_Merge_Two_Sorted_Lists import Solution, Arr


class SolutionTest(unittest.TestCase):

    def run_test(self, result, list1, list2):
        arr1 = Arr(list1)
        arr2 = Arr(list2)
        s = Solution()
        self.assertEqual(result, s.mergeTwoLists(arr1.head, arr2.head))

    def test_case_1(self):
        self.run_test([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 2, 4, 6, 8, 10], [1, 3, 5, 7, 9])

    def test_case_2(self):
        self.run_test([], [], [])

    def test_case_3(self):
        self.run_test([-10, -4, -3, 0, 2, 5], [-10, 5], [-4, -3, 0, 2])

    def test_case_4(self):
        self.run_test([1, 2], [], [1, 2])

    def test_case_5(self):
        self.run_test([-10], [-10], [])

    def test_case_6(self):
        self.run_test([1, 2, 3], [1, 2], [3])

    def test_case_7(self):
        self.run_test([-100, 10, 19], [10, 19], [-100])

    def test_case_8(self):
        self.run_test([1, 1, 2, 3, 4, 4], [1, 2, 4], [1, 3, 4])

    def test_case_9(self):
        self.run_test([1, 1, 2, 2, 4, 4], [1, 2, 4], [1, 2, 4])


if __name__ == "__main__":
    unittest.main()
