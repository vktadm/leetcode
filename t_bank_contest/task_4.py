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

    def solution(self, data_in, data_out):
        n, k = map(int, data_in[0].split())
        num_lst = list(map(int, data_in[1].split()))

        initial_sum = sum(num_lst)

        # Список для хранения возможных увеличений
        increases = []

        # Проходим по каждому числу
        for number in num_lst:
            str_number = str(number)
            for digit in reversed(str_number):
                # Вычисляем возможное увеличение при замене на 9
                increase = 9 - int(digit)
                if increase > 0:
                    increases.append(increase)

        # Сортируем увеличения по убыванию
        increases.sort(reverse=True)

        # Максимальное увеличение суммы
        max_increase = sum(increases[:k])

        # Возвращаем разность между новой и старой суммой
        print(max_increase)

if __name__ == "__main__":
    s = Solution()
    s.solution(['5 2', '1 135  23  3  5'], '16')
    # unittest.main()