from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hmap = dict()

        for itm in arr:
            if itm in hmap:
                hmap[itm] += 1
            else:
                hmap[itm] = 1

        return len(set(hmap.values())) == len(hmap.keys())
