import timeit
from typing import List


class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]] | List:
        events = []

        for itm in range(len(firstList)):
            events.append((firstList[itm][0], -1))
            events.append((firstList[itm][1], 1))
        for itm in range(len(secondList)):
            events.append((secondList[itm][0], -1))
            events.append((secondList[itm][1], 1))

        events.sort()

        intersection = 0
        result = []
        new_intersection = []

        for itm in range(len(events)):
            if events[itm][1] == -1:
                intersection += 1
                if intersection == 2:
                    new_intersection.append(events[itm][0])
            if events[itm][1] == 1:
                if intersection == 2:
                    new_intersection.append(events[itm][0])
                    result.append(new_intersection)
                    new_intersection = []
                intersection -= 1

        return result

    def intervalIntersection_fast(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]] | List:
        res = []

        p1 = p2 = 0

        while p1 < len(firstList) and p2 < len(secondList):
            l = max(firstList[p1][0], secondList[p2][0])
            r = min(firstList[p1][1], secondList[p2][1])

            if l <= r:
                res.append([l, r])

            if firstList[p1][1] < secondList[p2][1]:
                p1 += 1
            else:
                p2 += 1

        return res


if __name__ == "__main__":
    firstList = [[idx, idx + 1] for idx in range(10000)]
    secondList = [[idx + 1, idx + 5] for idx in range(10000)]
    s = Solution()
    print(s.intervalIntersection(firstList, secondList))
    print(s.intervalIntersection_fast(firstList, secondList))
    s_time = (
        timeit.timeit(
            "s.intervalIntersection(firstList, secondList)",
            globals=globals(),
            number=100,
        )
        / 100
    )
    s_time_fast = (
        timeit.timeit(
            "s.intervalIntersection_fast(firstList, secondList)",
            globals=globals(),
            number=100,
        )
        / 100
    )
    print(f"Время - intervalIntersection: {s_time} секунд")
    print(f"Время - intervalIntersection_fast: {s_time_fast} секунд")
