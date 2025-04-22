from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {}

        for idx in range(len(s)):
            last_occurrence[s[idx]] = idx

        result = []
        start = 0
        end = 0

        for idx in range(len(s)):
            end = max(end, last_occurrence[s[idx]])

            if idx == end:
                result.append(end - start + 1)
                start = idx + 1

        return result


print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
