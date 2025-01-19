class Solution(object):
    """Given a pattern and a string s, find if s follows the same pattern.

    Input: pattern = "abba", s = "dog cat cat dog"
    Output: true

    Input: pattern = "abba", s = "dog cat cat fish"
    Output: false
    """
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split()

        if len(pattern) != len(s):
            return False

        pattern_map = {}
        s_map = []

        for num in range(len(pattern)):
            if pattern[num] in pattern_map:
                if pattern_map[pattern[num]] != s[num]:
                    return False
            else:
                if s[num] in s_map:
                    return False
                else:
                    pattern_map[pattern[num]] = s[num]
                    s_map.append(s[num])
        return True