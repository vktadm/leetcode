from typing import List, Tuple


def in_bound(i: int, j: int, matrix: List[List[int]]) -> bool:
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[i])


def dfs(
    i: int,
    j: int,
    end: Tuple[int, int],
    used: List[List[bool]],
    matrix: List[List[int]],
) -> bool:
    if not in_bound(i, j, matrix) or matrix[i][j] == 1 or used[i][j]:
        return False

    used[i][j] = True
    if (i, j) == end:
        return True

    return (
        dfs(i - 1, j, end, used, matrix)  # вверх
        or dfs(i, j + 1, end, used, matrix)  # вправо
        or dfs(i + 1, j, end, used, matrix)  # вниз
        or dfs(i, j - 1, end, used, matrix)  # влево
    )


def has_path(
    matrix: List[List[int]],
    start: Tuple[int, int],
    end: Tuple[int, int],
) -> bool:
    used = [[False for _ in range(len(row))] for row in matrix]
    return dfs(start[0], start[1], end, used, matrix)


if __name__ == "__main__":
    matrix = [[0, 0, 0, 1], [1, 0, 0, 1], [0, 0, 0, 0], [0, 1, 1, 0]]
    print(has_path(matrix, (0, 0), (3, 3)))  # True или False
