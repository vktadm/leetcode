def solve(numbers):
    result = [None] * len(numbers)
    stack = []

    for idx in range(len(numbers)):
        stack.append((numbers[idx], idx))
        if stack:
            for s_idx in reversed(range(0, len(stack) - 1)):
                if stack[-1][0] < stack[s_idx][0]:
                    popped = stack.pop(s_idx)
                    result[popped[1]] = stack[-1][1]

    while stack:
        popped = stack.pop()
        result[popped[1]] = len(numbers)

    return result


numbers = '7 2 4 5 3 2 5 1 5 4'
result = solve(list(map(int, numbers.split())))
print(*result)
