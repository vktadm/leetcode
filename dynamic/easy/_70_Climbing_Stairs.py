class Solution:
    def climbStairs(self, n: int) -> int:
        base = [0, 1]
        for idx in range(n):
            new_value = base[0] + base[1]
            base = base[1], new_value

        return base[1]


if __name__ == "__main__":
    print(Solution().climbStairs(4))
