class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s) - 1

        while start < end:
            # if not s[start].isascii():
            if not s[start].isalpha() and not s[start].isdigit():
                start += 1
                continue
            # if not s[end].isascii():
            if not s[end].isalpha() and not s[end].isdigit():
                end -= 1
                continue

            if s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1

        return True