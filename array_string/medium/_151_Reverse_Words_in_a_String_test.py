import unittest

from ._151_Reverse_Words_in_a_String import Solution


class SolutionTest(unittest.TestCase):

    def run_test(self, s: str, result: str):
        self.assertEqual(result, Solution().reverseWords(s))

    def test_case_1(self):
        self.run_test("the sky is blue", "blue is sky the")

    def test_case_2(self):
        self.run_test("  hello world  ", "world hello")

    def test_case_3(self):
        self.run_test("a good   example", "example good a")


if __name__ == "__main__":
    unittest.main()
