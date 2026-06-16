from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup_map = {}
        for itm in range(len(nums)):
            if dup_map.get(nums[itm], None) is not None:
                return True

            dup_map[nums[itm]] = 1

        return False
