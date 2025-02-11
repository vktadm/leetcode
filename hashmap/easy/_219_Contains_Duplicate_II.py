class Solution(object):
    """
    nums[i] == nums[j] and abs(i - j) <= k
    """
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if (len(nums) == len(set(nums))): return False

        nums_map = {}

        for idx in range(len(nums)):
            if nums[idx] in nums_map and abs(idx - nums_map[nums[idx]]) <= k:
                return True
            nums_map[nums[idx]] = idx
        return False


