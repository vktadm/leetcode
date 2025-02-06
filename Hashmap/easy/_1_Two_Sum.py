class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diff_nums = {}
        l = len(nums)

        for idx in range(l):
            diff_nums[target - nums[idx]] = idx

        for idx in range(l):
            value = nums[idx]
            if diff_nums.get(value) and idx != diff_nums[value]:
                return [idx, diff_nums[nums[idx]]]


s = Solution()
print(s.twoSum([1, 3, 4, 2], 6))
