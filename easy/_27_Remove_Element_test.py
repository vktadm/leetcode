import unittest
from . import _27_Remove_Element as rm

class RemoveElementTest(unittest.TestCase):

    def delite(self, nums, val):
        k = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
                k += 1
            else:
                i += 1

    def run_remove(self, nums, val):
        std_nums = nums
        self.delite(std_nums, val)

        rm_class = rm.Solution()
        rm_class.removeElement(nums, val)

        self.assertEqual(std_nums, nums)

    def test_case_1(self):
        self.run_remove([3, 2, 2, 3], 2)
    def test_case_2(self):
        self.run_remove([0, 1, 2, 2, 3, 0, 4, 2], 2)
    # def test_case_3(self):
    #     self.run_merge([0], 0, [3], 1)


if __name__ == "__main__":
    unittest.main()