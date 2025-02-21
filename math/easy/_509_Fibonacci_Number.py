class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0, 1]

        if n in f:
            return f[n]

        for _ in range(1, n):
            new_f = f[1] + f[0]
            f[0], f[1] = f[1], new_f

        return f[1]


print(Solution().fib(10000))
