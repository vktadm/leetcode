from collections import Counter, defaultdict
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        length = len(words[0])
        word_count = Counter(words)
        indexes = []

        for i in range(length):
            start = i
            window = defaultdict(int)
            words_used = 0

            for j in range(i, len(s) - length + 1, length):
                word = s[j : j + length]

                if word not in word_count:
                    start = j + length
                    window = defaultdict(int)
                    words_used = 0
                    continue

                words_used += 1
                window[word] += 1

                while window[word] > word_count[word]:
                    window[s[start : start + length]] -= 1
                    start += length
                    words_used -= 1

                if words_used == len(words):
                    indexes.append(start)

        return indexes


if __name__ == "__main__":
    solution = Solution()
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    result = [0, 9]
    assert solution.findSubstring(s, words) == result
    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "word"]
    result = []
    assert solution.findSubstring(s, words) == result
    s = "barfoofoobarthefoobarman"
    words = ["bar", "foo", "the"]
    result = [6, 9, 12]
    assert solution.findSubstring(s, words) == result
