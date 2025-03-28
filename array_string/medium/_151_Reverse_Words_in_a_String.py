class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
        # result = []
        # idx = l = len(s) - 1
        # word = ""
        #
        # while idx >= 0:
        #     if s[idx] != " ":
        #         word += s[idx]
        #     if word and (s[idx] == " " or idx == 0):
        #         result.append(word[::-1])
        #         word = ""
        #     idx -= 1
        # return " ".join(result)
