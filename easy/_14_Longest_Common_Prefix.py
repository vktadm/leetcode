class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        prefix = strs[0]

        for string in strs[1:]:
            while string[:len(prefix)] != prefix and prefix:
                prefix = prefix[:-1]  # Remove last character from prefix

            if not prefix:
                return ""

        return prefix