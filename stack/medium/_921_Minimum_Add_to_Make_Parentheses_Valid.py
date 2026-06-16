import unittest


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened = 0
        closed = 0
        for item in s:
            if item == "(":
                opened += 1
            elif opened:
                opened -= 1
            else:
                closed += 1

        return closed + opened


class TestMinAddToMakeValid(unittest.TestCase):
    def test_example_1(self):
        """Test from Example 1: '())' should return 1"""
        self.assertEqual(Solution().minAddToMakeValid("())"), 1)

    def test_example_2(self):
        """Test from Example 2: '(((' should return 3"""
        self.assertEqual(Solution().minAddToMakeValid("((("), 3)

    def test_empty_string(self):
        """Empty string is already valid"""
        self.assertEqual(Solution().minAddToMakeValid(""), 0)

    def test_already_valid_simple(self):
        """Already valid simple parentheses"""
        self.assertEqual(Solution().minAddToMakeValid("()"), 0)

    def test_already_valid_nested(self):
        """Already valid nested parentheses"""
        self.assertEqual(Solution().minAddToMakeValid("(())"), 0)

    def test_already_valid_multiple_pairs(self):
        """Already valid multiple pairs"""
        self.assertEqual(Solution().minAddToMakeValid("()()"), 0)

    def test_only_opening(self):
        """String with only opening parentheses"""
        self.assertEqual(Solution().minAddToMakeValid("((((("), 5)

    def test_only_closing(self):
        """String with only closing parentheses"""
        self.assertEqual(Solution().minAddToMakeValid("))))"), 4)

    def test_mixed_unmatched(self):
        """Mixed parentheses with various unmatched patterns"""
        self.assertEqual(Solution().minAddToMakeValid("())("), 2)

    def test_alternating_unmatched(self):
        """Alternating parentheses that are unmatched"""
        self.assertEqual(Solution().minAddToMakeValid(")()("), 2)

    def test_start_with_closing(self):
        """String starting with closing parenthesis"""
        self.assertEqual(Solution().minAddToMakeValid(")()"), 1)

    def test_end_with_opening(self):
        """String ending with opening parenthesis"""
        self.assertEqual(Solution().minAddToMakeValid("()("), 1)

    def test_complex_pattern(self):
        """More complex pattern of parentheses"""
        self.assertEqual(Solution().minAddToMakeValid("())(()"), 2)

    def test_single_opening(self):
        """Single opening parenthesis"""
        self.assertEqual(Solution().minAddToMakeValid("("), 1)

    def test_single_closing(self):
        """Single closing parenthesis"""
        self.assertEqual(Solution().minAddToMakeValid(")"), 1)

    def test_long_valid_string(self):
        """Long already valid string"""
        self.assertEqual(Solution().minAddToMakeValid("(((())))()()"), 0)

    def test_deeply_nested_unmatched(self):
        """Deeply nested but unmatched parentheses"""
        self.assertEqual(Solution().minAddToMakeValid("(((()"), 3)

    def test_closing_then_opening_repeated(self):
        """Pattern: )()()()("""
        self.assertEqual(Solution().minAddToMakeValid(")()()()("), 2)

    def test_all_unmatched_pairs_reversed(self):
        """All parentheses in wrong order: )))((("""
        self.assertEqual(Solution().minAddToMakeValid(")))((("), 6)


if __name__ == "__main__":
    unittest.main()
