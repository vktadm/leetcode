class Solution(object):
    """
    Given two strings needle and haystack, return the index of the first
    occurrence of needle in haystack, or -1 if needle is not part of haystack.

    Input: haystack = "sadbutsad", needle = "sad"
    Output: 0
    Explanation: "sad" occurs at index 0 and 6.
    The first occurrence is at index 0, so we return 0.
    """

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0

        # Get lengths of haystack and needle
        haystack_length = len(haystack)
        needle_length = len(needle)

        # Loop through the haystack
        for i in range(haystack_length - needle_length + 1):
            # Check if the substring matches the needle
            if haystack[i:i + needle_length] == needle:
                return i  # Return the starting index if found

        return -1