class Solution(object):
    """"Merge nums1 and nums2 into a single array sorted in non-decreasing order."""
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        nums1_index, nums2_index, write_index = m - 1, n - 1, m + n - 1

        while nums2_index >= 0:
            if nums1_index >= 0 and nums1[nums1_index] > nums2[nums2_index]:
                nums1[write_index] = nums1[nums1_index]
                nums1_index -= 1
            else:
                nums1[write_index] = nums2[nums2_index]
                nums2_index -= 1
            write_index -= 1



