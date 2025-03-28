from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [
            0,
        ]
        for idx in range(0, len(gain)):
            altitudes.append(altitudes[idx] + gain[idx])

        return max(altitudes)
