import unittest

from _20_Valid_Parentheses import Solution


class SolutionTest(unittest.TestCase):

    def run_test(self, result, s):
        self.assertEqual(result, Solution().isValid(s))

    def test_case_1(self):
        self.run_test(True, "()")

    def test_case_2(self):
        self.run_test(True, "()[]{}")

    def test_case_3(self):
        self.run_test(False, "(]")

    def test_case_4(self):
        self.run_test(True, "([])")

    def test_case_5(self):
        self.run_test(False, "([])[}")

    def test_case_6(self):
        self.run_test(True, "([([[]])])[{{(())}}]")

    def test_case_6(self):
        self.run_test(False, "(){}[[]")

    def test_case_7(self):
        self.run_test(False, "]")


if __name__ == "__main__":
    unittest.main()
