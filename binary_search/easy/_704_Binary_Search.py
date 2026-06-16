from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        end = len(nums) - 1
        start = 0
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return -1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(Solution().search(nums, target))
