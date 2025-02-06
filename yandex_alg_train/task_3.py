import unittest

class Solution:
    "Задача: 'Надпись на табло'"

    def compress(self, lst):
        result = [[lst[0]]]
        for new_lst in lst[1:]:
            if new_lst != result[-1]:
                result.append(new_lst)
        if len(result) > 1 and set(result[0]) == {'.'}:
            result.pop(0)
        if len(result) > 1 and set(result[-1]) == {'.'}:
            result.pop()
        return result

    def invert(self, lst):
        result = [[] for _ in range(len(lst[0]))]
        for new_lst in lst:
            for i in range(len(new_lst)):
                result[i].append(new_lst[i])

        for i in range(len(result)):
            result[i] = ''.join(result[i])

        return result



# class Task3(unittest.TestCase):
#
#     def run_test(self):
#         self.assertEqual()
#
#     def test_case_1(self):
#         self.run_test()
#
#     def test_case_2(self):
#         self.run_test()
#
#     def test_case_3(self):
#         self.run_test()


if __name__ == "__main__":
    # unittest.main()
    with open('input_task_3.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    tests = []
    test = []

    for itm in range(len(lines)):
        if 'test' in lines[itm].lower() or itm == len(lines) - 1:
            tests.append(test)
        if '#' in lines[itm].strip() and '.' in lines[itm].strip():
            test.append(lines[itm].replace('\n', ''))

    for row in tests:
        print(row)