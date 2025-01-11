import unittest

from Array_String.easy._28_Index_First_Occurrence_String import Solution


class FirstOccurrenceStr(unittest.TestCase):

    def best_solve(self, haystack, needle):
        return haystack.find(needle)

    def run_longest_prefix(self, haystack, needle):
        self.assertEqual(self.best_solve(haystack, needle), Solution().strStr(haystack, needle))


    def test_case_1(self):
        self.run_longest_prefix("dhhsadbutsad", "sad")

    def test_case_2(self):
        self.run_longest_prefix("leetcode", "leeto")

    def test_case_3(self):
        self.run_longest_prefix("hh", "h")

    def test_case_4(self):
        self.run_longest_prefix("", "")

    def test_case_5(self):
        self.run_longest_prefix("mississippi", "issip")


if __name__ == "__main__":
    unittest.main()