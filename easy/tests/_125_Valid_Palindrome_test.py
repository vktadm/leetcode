import unittest

from easy._125_Valid_Palindrome import Solution


class TestClass(unittest.TestCase):

    def best_solve(self, s):
        s = ''.join(filter(str.isascii, s.lower()))
        return True if s == s[::-1] else False

    def run_test(self, s):
        self.assertEqual(self.best_solve(s), Solution().isPalindrome(s))


    def test_case_1(self):
        self.run_test("A man, a plan, a canal: Panama")

    def test_case_2(self):
        self.run_test("race a car")

    def test_case_3(self):
        self.run_test(" ")

    def test_case_4(self):
        self.run_test("0P")


if __name__ == "__main__":
    unittest.main()