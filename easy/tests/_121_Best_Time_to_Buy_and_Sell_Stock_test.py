import unittest
from easy._121_Best_Time_to_Buy_and_Sell_Stock import Solution


class MajorityTest(unittest.TestCase):

    def best_solve(self, prices):
        buy = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy

        return profit

    def run_best_time(self, prices):
        self.assertEqual(self.best_solve(prices), Solution().maxProfit(prices))

    def test_case_1(self):
        self.run_best_time([7, 2, 6, 1, 3, 4])

    def test_case_2(self):
        self.run_best_time([7, 6, 4, 3, 1])

    def test_case_3(self):
        self.run_best_time([1, 2, 3, 4, 5, 6])

    def test_case_4(self):
        self.run_best_time([2, 1, 2, 1, 0, 1, 2])


if __name__ == "__main__":
    unittest.main()
