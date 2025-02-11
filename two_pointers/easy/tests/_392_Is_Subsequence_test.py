import unittest

from two_pointers.easy._392_Is_Subsequence import Solution


class TestClass(unittest.TestCase):

    def best_solve(self, s, t):
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return True if i == len(s) else False


    def run_test(self, s, t):
        self.assertEqual(self.best_solve(s, t), Solution().isSubsequence(s, t))

    def test_case_1(self):
        self.run_test("abba", "abba")

    def test_case_2(self):
        self.run_test("abc", "ahbgdc")

    def test_case_3(self):
        self.run_test("ab", "baab")

    def test_case_5(self):
        self.run_test("", " ")

    def test_case_6(self):
        self.run_test("axc", "ahbgdc")


if __name__ == "__main__":
    unittest.main()