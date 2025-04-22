from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        distance = -1
        max_distance = 0
        for i in range(len(seats)):
            if seats[i]:
                if distance == -1:
                    max_distance = i
                else:
                    max_distance = max(max_distance, ((i - distance) // 2))
                distance = i

        if seats[-1] == 0:
            max_distance = max(max_distance, (len(seats) - 1 - distance))

        return max_distance


if __name__ == "__main__":
    seats = [1, 0, 0, 0, 0, 1, 0]
    print(Solution().maxDistToClosest(seats))
