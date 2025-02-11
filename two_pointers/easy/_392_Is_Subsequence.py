from sys import thread_info


class Solution(object):
    """
    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
    """
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":
            return True

        s_index = len(s) - 1
        t_index = len(t) - 1

        while t_index >= 0:
            if s[s_index] == t[t_index]:
                s_index -= 1

            if s_index == -1:
                return True

            t_index -= 1

        return False