import unittest

from Hashmap.easy._290_Word_Pattern import Solution


class SolutionTest(unittest.TestCase):

    def run_test(self, test_value, ransom_note, magazine):
        self.assertEqual(test_value, Solution().wordPattern(ransom_note, magazine))

    def test_case_1(self):
        self.run_test(True, "abba", "dog cat cat dog")

    def test_case_2(self):
        self.run_test(False, "abba", "dog cat cat fish")

    def test_case_3(self):
        self.run_test(False, "aaaa", "dog cat cat dog")

    def test_case_4(self):
        self.run_test(False, "aaa", "aa aa aa aa")


if __name__ == "__main__":
    unittest.main()