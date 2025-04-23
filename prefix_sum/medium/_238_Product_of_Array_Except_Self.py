from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        L = 1
        for i in range(n):
            answer[i] = L
            L *= nums[i]

        R = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= R
            R *= nums[i]

        return answer


nums = [-1, 1, 0, -3, 3]
print(Solution().productExceptSelf(nums))
