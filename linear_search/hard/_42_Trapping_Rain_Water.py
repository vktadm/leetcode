from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        max_position = 0  # Максимальный столбец
        # Ищем максмальную позицию вершины
        for i in range(len(height)):
            if height[i] > height[max_position]:
                max_position = i

        result = 0  # Результат
        new_max_position = 0  # Текущий максимум
        for i in range(max_position):
            if height[i] > new_max_position:
                new_max_position = height[i]
            result += new_max_position - height[i]

        new_max_position = 0
        for i in range(len(height) - 1, max_position, -1):
            if height[i] > new_max_position:
                new_max_position = height[i]
            result += new_max_position - height[i]

        return result


s = Solution()
heights = [4, 2, 0, 3, 2, 5]
print(s.trap(heights))
