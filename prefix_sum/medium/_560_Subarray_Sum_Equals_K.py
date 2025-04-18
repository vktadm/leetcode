from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pf_sum_counter = {0: 1}
        result = 0
        pf_sum = 0
        for num in nums:
            pf_sum = pf_sum + num
            if (pf_sum - k) in pf_sum_counter:
                result += pf_sum_counter[pf_sum - k]
            if pf_sum in pf_sum_counter:
                pf_sum_counter[pf_sum] += 1
            else:
                pf_sum_counter[pf_sum] = 1
        return result


nums = [1, 2, 0, 0, 0, 3, 2, 1]
k = 3
print(Solution().subarraySum(nums, k))
