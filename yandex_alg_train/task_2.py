import unittest

class Solution:
    "Задача: 'Майки и носки'"

    def solution(self, input_data):
        a, b, c, d = input_data
        result_lst = []

        if b > 0 and d > 0:
            result_lst.append([b + 1, d + 1])
        if a > 0 and c > 0:
            result_lst.append([a + 1, c + 1])
        if a > 0 and b > 0:
            result_lst.append([max(a, b) + 1, 1])
        if c > 0 and d > 0:
            result_lst.append([1, max(c, d) + 1])

        result = min(result_lst, key=sum)

        print(*result)

# class Task2(unittest.TestCase):
#
#     def run_test(self, input_data, result):
#         self.assertEqual(result, Solution().solution(input_data))
#
#     def test_case_1(self):
#         input_data = [-4, 3, -2, -1, 2, 1]
#         self.run_test(input_data, 'NW')

    # def test_case_2(self):
    #     input_data = [4, 3, -2, -1, 2, 1]
    #     self.run_test(input_data, 'NE')
    #
    # def test_case_3(self):
    #     input_data = [-4, -3, -2, -1, 2, 1]
    #     self.run_test(input_data, 'SW')


if __name__ == "__main__":
    # unittest.main()
    s = Solution()
    s.solution([4, 3, 5, 1])