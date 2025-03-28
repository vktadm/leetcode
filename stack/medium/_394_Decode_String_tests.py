import unittest

from ._394_Decode_String import Solution


class SolutionTest(unittest.TestCase):

    def run_test(self, s: str, result: str):
        self.assertEqual(result, Solution().decodeString(s))

    def test_case_1(self):
        self.run_test("3[a]2[bc]", "aaabcbc")

    def test_case_2(self):
        self.run_test("3[a2[c]]", "accaccacc")

    def test_case_3(self):
        self.run_test("2[abc]3[cd]ef", "abcabccdcdcdef")


if __name__ == "__main__":
    unittest.main()
