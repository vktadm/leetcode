class Solution(object):

    def calculation(self, value):
        s = 0
        while value:
            d = value % 10
            value = value // 10
            s += d * d
        return s

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        results = {n}

        while n != 1:
            new_n = self.calculation(n)
            if new_n in results:
                return False
            results.add(new_n)
            n = new_n
        return True



s = Solution()
print(s.isHappy(19))
