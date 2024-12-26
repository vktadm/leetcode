class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        index = 0
        size = len(nums)

        while index < size:
            if nums[index] == val:
                for j in range(index, size - k):
                    if j + 1 < size:
                        nums[j] = nums[j + 1]
                nums[size -1 - k] = None
                k += 1
                index -= 2
            index += 1