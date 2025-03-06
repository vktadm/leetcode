class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()

        prev = float("-inf")
        result = 0

        for itm in intervals:
            if itm[0] >= prev:
                prev = itm[1]
            else:
                result += 1
                prev = min(prev, itm[1])

        if len(intervals) == result:
            return result - 1

        return result
