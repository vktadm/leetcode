from collections import defaultdict
from typing import List
import unittest


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        values_map = defaultdict(int)
        for num in nums:
            values_map[num] += 1

        for key, value in values_map.items():
            if value == 1:
                return key

        return -1


class TestSingleNumber(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(Solution().singleNumber([2, 2, 3, 2]), 3)

    def test_example_2(self):
        self.assertEqual(Solution().singleNumber([0, 1, 0, 1, 0, 1, 99]), 99)

    def test_single_element(self):
        self.assertEqual(Solution().singleNumber([42]), 42)
        self.assertEqual(Solution().singleNumber([-5]), -5)

    def test_all_negative(self):
        self.assertEqual(Solution().singleNumber([-1, -1, -1, -5]), -5)
        self.assertEqual(Solution().singleNumber([-10, -10, -10, 7, 7, 7, -999]), -999)

    def test_mixed_signs(self):
        self.assertEqual(Solution().singleNumber([1, 1, 1, -1, -1, -1, 42]), 42)

    def test_zero(self):
        self.assertEqual(Solution().singleNumber([0, 0, 0, 1, 1, 1, 0]), -1)
        self.assertEqual(Solution().singleNumber([1, 1, 1, 0]), 0)

    def test_large_numbers(self):
        self.assertEqual(
            Solution().singleNumber([2**31 - 1, 2**31 - 1, 2**31 - 1, -(2**31)]),
            -(2**31),
        )

    def test_multiple_groups(self):
        self.assertEqual(Solution().singleNumber([1, 1, 1, 2, 2, 2, 3, 3, 3, 4]), 4)

    def test_long_array(self):
        nums = [5] * 99 + [7] * 3 + [123]
        nums = nums[50:] + nums[:50]  # shuffle a bit
        self.assertEqual(Solution().singleNumber(nums), 123)

    def test_min_max_int(self):
        self.assertEqual(
            Solution().singleNumber([2**31 - 1] * 3 + [-(2**31)]), -(2**31)
        )

    def test_edge_case_empty(self):
        # According to problem constraints, nums is non-empty
        with self.assertRaises(Exception):
            Solution().singleNumber([])


if __name__ == "__main__":
    unittest.main()
