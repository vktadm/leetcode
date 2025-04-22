from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        zeros = 0
        result = 0

        for right in range(n):
            if not nums[right]:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            result = max(result, right - left + 1 - zeros)

        return result - 1 if result == n else result


if __name__ == "__main__":
    nums = [0, 1, 1, 1]
    print(Solution().longestSubarray(nums))
