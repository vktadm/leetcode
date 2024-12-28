import unittest
from . import _88_Merge_Sorted_Array as ms

class MergeSortedTest(unittest.TestCase):

    def run_merge(self, nums1, m,  nums2, n):
        std_nums1, std_nums2 = nums1, nums2
        std_nums1 = std_nums1[0:m] + std_nums2
        std_nums1.sort()

        merge_class = ms.Solution()
        merge_class.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, std_nums1)

    def test_case_1(self):
        self.run_merge([8, 9, 10, 0, 0, 0], 3, [1, 2, 3], 3)
    def test_case_2(self):
        self.run_merge([1], 1, [], 0)
    def test_case_3(self):
        self.run_merge([0], 0, [3], 1)


if __name__ == "__main__":
    unittest.main()