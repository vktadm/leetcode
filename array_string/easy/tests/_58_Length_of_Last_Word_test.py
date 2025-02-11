import unittest

from array_string.easy._58_Length_of_Last_Word import Solution


class LengthOfLastWordTest(unittest.TestCase):

    def functions_solve(self, input_string):
        return len(input_string.split()[-1])


    def run_lenght_last(self, roman_str):
        self.assertEqual(self.functions_solve(roman_str), Solution().lengthOfLastWord(roman_str))

    def test_case_1(self):
        self.run_lenght_last("Hello World")

    def test_case_2(self):
        self.run_lenght_last("   fly me   to   the moon  ")

    def test_case_3(self):
        self.run_lenght_last("luffy is still joyboy")


if __name__ == "__main__":
    unittest.main()