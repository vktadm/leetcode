class Solution(object):
    """
    Converting Roman to int.
    Input: s = "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    """
    def romanToInt(self, roman_str):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0
        curr_value = 0

        # Проходим по строке справа налево
        for char in reversed(roman_str):
            curr_value = roman_map[char]

            # Если текущее значение меньше предыдущего, вычитаем его, иначе добавляем
            if curr_value < prev_value:
                total -= curr_value
            else:
                total += curr_value

            # Обновляем предыдущее значение
            prev_value = curr_value

        return total

if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("MCMXCIV"))
    