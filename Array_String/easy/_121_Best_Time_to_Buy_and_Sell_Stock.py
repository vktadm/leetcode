class Solution(object):
    """
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_price = None
        difference = 0

        iter = 0
        while iter < len(prices):
            if prices[iter] < min_price:
                min_price = prices[iter]
                max_price = None
            elif min_price < prices[iter]:
                max_price = prices[iter]

            if max_price:
                if (max_price - min_price) > difference:
                    difference = max_price - min_price
            iter += 1

        return difference