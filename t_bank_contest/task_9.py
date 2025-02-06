from time import time

# import unittest
#
# class Task4(unittest.TestCase):
#
#     def run_test(self, data_in, data_out):
#         self.assertEqual(data_out, Solution().solution())
#
#     def test_case_1(self):
#         self.run_test(['5 2', '1  2  1  3  5'], '16')
#
#     def test_case_2(self):
#         self.run_test(['3  1', '99  5  85'], '10')
#
#     def test_case_2(self):
#         self.run_test(['1  10', '9999'], '0')


class Solution:
    # TODO

    def solution(self, data_in):
        n, *costs = map(int, data_in)

        benefit = None
        min_pay = None


if __name__ == "__main__":
    s = Solution()
    s.solution(['5', '35', '40', '101', '59', '63'])
    # unittest.main()