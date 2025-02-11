# class Counter():
#     """Counter for array elements."""
#     def __init__(self, size):
#         self.counts = [0] * (size + 1)
#         self.size = size + 1
# class Solution(Counter):
#     """Solution of task."""
#     def __init__(self, nums):
#         self.data = nums
#         super().__init__(max(nums))
#     def majorityElement(self):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         for value in self.data:
#             self.counts[value] += 1
#         self.counts = map(lambda val: True if val >= (self.size / 2) else False, self.counts)
#
#         return list(self.counts).index(True)

class Solution(object):
    """Solution of task."""
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = max(nums) + 1
        counts = [0] * size

        for value in nums:
            counts[value] += 1

        index = 0
        for count in counts:
            if count >= ((len(nums) + 1) // 2):
                return index
            index += 1
        return None