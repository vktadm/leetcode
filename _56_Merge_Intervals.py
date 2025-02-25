class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return intervals

        intervals.sort(key=lambda x: x[0])

        idx = 1

        while idx < len(intervals):
            current = intervals[idx]
            previous = intervals[idx - 1]

            if previous[0] <= current[0] <= previous[1]:
                popped = intervals.pop(idx)
                previous[1] = max(popped[1], previous[1])
                idx -= 1

            idx += 1

        return intervals





