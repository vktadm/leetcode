import unittest

class MergeSortedTest(unittest.TestCase):

    def run_merge(self, array_1, array_2):
        standart_merge = sorted(array_1 + array_2)
        my_merge = Solution()
        self.assertEqual(standart_merge, )

    def test_case_1(self):
        self.run_sort([10, 9, 8])

    def test_case_2(self):
        self.run_sort([10, 8, 9])


if __name__ == "__main__":
    unittest.main()
