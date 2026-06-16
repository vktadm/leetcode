from curses.ascii import isalpha
from typing import List


class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0
        for item in prices[1:]:
            if buy_price > item:
                buy_price = item

            profit = max(profit, item - buy_price)

        return profit


"".isd
