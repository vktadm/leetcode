from curses.ascii import isalpha


class Solution(object):
    def lengthOfLastWord(self, input_string):
        """
        Given a string s consisting of words and spaces,
        return the length of the last word in the string.

        Input: s = "Hello World"
        Output: 5
        Explanation: The last word is "World" with length 5.

        :type s: str
        :rtype: int
        """
        cnt = 0
        prev_symbol= ""

        for symbol in input_string:
            if symbol.isalpha():
                if prev_symbol == " ":
                    cnt = 0
                cnt += 1

            prev_symbol = symbol

        return cnt