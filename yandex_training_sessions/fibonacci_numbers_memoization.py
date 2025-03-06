def fib(n: int, dp: list) -> int:
    # Рекурсивная ф-ия
    if dp[n] == -1:
        dp[n] = fib(n - 1, dp) + fib(n - 2, dp)
    return dp[n]


def fib_loop(n: int, dp: list) -> int:
    # С циклом
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]


n = int(input("Введите номер числа Фибоначчи: "))

dp = [-1] * (n + 1)
dp[0] = dp[1] = 1
print(fib(n, dp))

dp = [0] * (n + 1)
dp[0] = dp[1] = 1
print(fib_loop(n, dp))
