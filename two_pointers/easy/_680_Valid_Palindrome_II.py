class Solution:
    @staticmethod
    def isPalindrome(s: str, start: int, end: int) -> bool:
        while start <= end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False

        return True

    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start <= end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return self.isPalindrome(s, start + 1, end) or self.isPalindrome(
                    s, start, end - 1
                )

        return True


if __name__ == "__main__":
    s = "aba"
    print(Solution().validPalindrome(s))
