import unittest

from easy._14_Longest_Common_Prefix import Solution


class LongestCommonPrefixTest(unittest.TestCase):

    def best_solve(self, strs):
        if not strs:
            return ""

        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) > 1:  # If there's a mismatch
                return strs[0][:i]

        return min(strs)


    def run_longest_prefix(self, list_string):
        self.assertEqual(self.best_solve(list_string), Solution().longestCommonPrefix(list_string))

    def test_case_1(self):
        self.run_longest_prefix(["flower", "flow", "flight"])

    def test_case_2(self):
        self.run_longest_prefix(["dog", "racecar", "car"])


if __name__ == "__main__":
    unittest.main()