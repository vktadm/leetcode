from collections import deque
from typing import List, Tuple


def in_bound(i: int, j: int, matrix: List[List[int]]) -> bool:
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[i])


def bfs(
    matrix: List[List[int]],
    start: Tuple[int, int],
    end: Tuple[int, int],
) -> int:
    # Инициализация расстояний (-1 = не посещено)
    dist = [[-1] * len(matrix[i]) for i in range(len(matrix))]

    dist[start[0]][start[1]] = 0  # стартовая точка
    q = deque([(start[0], start[1])])

    while q:
        x, y = q.popleft()

        if (x, y) == end:
            return dist[x][y]

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if in_bound(nx, ny, matrix) and matrix[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    # путь не найден
    return -1


if __name__ == "__main__":
    matrix = [[0, 0, 0, 1], [1, 0, 0, 1], [0, 0, 0, 0], [0, 1, 1, 0]]

    start = (0, 0)
    end = (3, 3)

    result = bfs(matrix, start, end)
    print(result)  # вернёт длину кратчайшего пути или -1
