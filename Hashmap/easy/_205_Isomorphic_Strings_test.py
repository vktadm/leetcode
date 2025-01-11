import unittest
from collections import Counter

from Hashmap.easy._205_Isomorphic_Strings import Solution


class SolutionTest(unittest.TestCase):

    def easy_solve(self, s, t):
        s_counter = Counter(s)
        t_counter = Counter(t)

        if list(s_counter.values()) != list(t_counter.values()):
            return False

        return True

    def run_test(self, s, t):
        self.assertEqual(self.easy_solve(s, t), Solution().isIsomorphic(s, t))

    def test_case_1(self):
        self.run_test("egg", "add")

    def test_case_2(self):
        self.run_test("foo", "bar")

    def test_case_3(self):
        self.run_test("paper", "title")


if __name__ == "__main__":
    unittest.main()