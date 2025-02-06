import unittest

class Solution:
    "Задача: 'Плот'"

    def solution(self, input_data):
        x, y, x1, y1, x2, y2 = input_data
        result = ''

        if y > y2:
            result += 'N'
        if y < y1:
            result += 'S'
        if x > x2:
            result += 'E'
        if x < x1:
            result += 'W'

        return result

class Task1(unittest.TestCase):

    def run_test(self, input_data, result):
        self.assertEqual(result, Solution().solution(input_data))

    def test_case_1(self):
        input_data = [-4, 3, -2, -1, 2, 1]
        self.run_test(input_data, 'NW')

    def test_case_2(self):
        input_data = [4, 3, -2, -1, 2, 1]
        self.run_test(input_data, 'NE')

    def test_case_3(self):
        input_data = [-4, -3, -2, -1, 2, 1]
        self.run_test(input_data, 'SW')


if __name__ == "__main__":
    unittest.main()