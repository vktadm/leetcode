from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in groups:
                groups[sorted_word] = []
            groups[sorted_word].append(word)

        result = []
        for sorted_word in groups:
            result.append(groups[sorted_word])

        return result


s = Solution()
words = ["a"]
print(s.groupAnagrams(words))
