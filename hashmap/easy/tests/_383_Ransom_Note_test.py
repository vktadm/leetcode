import unittest

from hashmap.easy._383_Ransom_Note import Solution


class SolutionTest(unittest.TestCase):

    def library_solve(self, ransom_note, magazine):
        if ransom_note > magazine:
            return False
        return True if ''.join(sorted(ransom_note)) in ''.join(sorted(magazine)) else False

    def run_test(self, ransom_note, magazine):
        self.assertEqual(self.library_solve(ransom_note, magazine), Solution().canConstruct(ransom_note, magazine))

    def test_case_1(self):
        self.run_test("a", "b")

    def test_case_2(self):
        self.run_test("aa", "ab")

    def test_case_3(self):
        self.run_test("aa", "aab")


if __name__ == "__main__":
    unittest.main()