from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for idx in range(len(nums)):
            diff = target - nums[idx]
            if diff in num_map:
                return [num_map[diff], idx]

            num_map[nums[idx]] = idx

        return []


if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    Solution().twoSum(nums, target)
