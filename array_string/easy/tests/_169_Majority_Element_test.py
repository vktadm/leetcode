import unittest
from array_string.easy import _169_Majority_Element as me


class MajorityTest(unittest.TestCase):

    def solve(self, nums):
        count = 0
        number = None

        for num in nums:
            if count == 0:
                number = num
            if num == number:
                count += 1
            else:
                count -= 1
        return number
    def run_majority(self, nums):
        self.assertEqual(self.solve(nums), me.Solution().majorityElement(nums))

    def test_case_1(self):
        self.run_majority([3, 2, 3])
    def test_case_2(self):
        self.run_majority([2, 2, 1, 1, 1, 2, 2])
    def test_case_3(self):
        self.run_majority([4, 5, 4])


if __name__ == "__main__":
    unittest.main()