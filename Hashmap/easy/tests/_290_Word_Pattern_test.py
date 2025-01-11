import unittest

from Hashmap.easy._290_Word_Pattern import Solution


class SolutionTest(unittest.TestCase):

    def library_solve(self, pattern, s):
        hashmap = list(zip(list(pattern), s.split()))


    def run_test(self, ransom_note, magazine):
        print(self.library_solve(ransom_note, magazine))
        # self.assertEqual(self.library_solve(ransom_note, magazine), Solution().wordPattern(ransom_note, magazine))

    def test_case_1(self):
        self.run_test("abba", "dog cat cat dog")

    def test_case_2(self):
        self.run_test("abba", "dog cat cat fish")

    def test_case_3(self):
        self.run_test("aaaa", "dog cat cat dog")


if __name__ == "__main__":
    unittest.main()