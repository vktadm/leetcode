class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_map = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        for itm in s:
            if itm in ["(", "{", "["]:
                stack.append(itm)
            elif stack and brackets_map.get(itm) == stack[-1]:
                stack.pop()
            else:
                return False

        return False if len(stack) > 0 else True


import unittest


class TestValidParentheses(unittest.TestCase):
    def test_example_1_simple_parentheses(self):
        """Тест 1: Простые круглые скобки"""
        self.assertTrue(Solution().isValid("()"))

    def test_example_2_multiple_types(self):
        """Тест 2: Несколько типов скобок"""
        self.assertTrue(Solution().isValid("()[]{}"))

    def test_example_3_mismatched(self):
        """Тест 3: Несовпадающие скобки"""
        self.assertFalse(Solution().isValid("(]"))

    def test_example_4_nested(self):
        """Тест 4: Вложенные скобки"""
        self.assertTrue(Solution().isValid("([])"))

    def test_example_5_incorrect_nested(self):
        """Тест 5: Неправильно вложенные скобки"""
        self.assertFalse(Solution().isValid("([)]"))

    def test_empty_string(self):
        """Тест 6: Пустая строка"""
        self.assertTrue(Solution().isValid(""))

    def test_single_open_bracket(self):
        """Тест 7: Одна открывающая скобка"""
        self.assertFalse(Solution().isValid("("))

    def test_single_close_bracket(self):
        """Тест 8: Одна закрывающая скобка"""
        self.assertFalse(Solution().isValid(")"))

    def test_all_open_brackets(self):
        """Тест 9: Только открывающие скобки"""
        self.assertFalse(Solution().isValid("({["))

    def test_all_close_brackets(self):
        """Тест 10: Только закрывающие скобки в правильном порядке"""
        self.assertFalse(Solution().isValid(")}]"))

    def test_deep_nesting(self):
        """Тест 11: Глубоко вложенные скобки"""
        self.assertTrue(Solution().isValid("({[]})"))

    def test_multiple_nested_groups(self):
        """Тест 12: Несколько вложенных групп"""
        self.assertTrue(Solution().isValid("({[]})({[]})"))

    def test_sequential_brackets(self):
        """Тест 13: Последовательные пары скобок"""
        self.assertTrue(Solution().isValid("()()()"))

    def test_complex_mixed(self):
        """Тест 14: Сложная смешанная последовательность"""
        self.assertTrue(Solution().isValid("{[()]}{[()]}"))

    def test_incorrect_order_close_brackets(self):
        """Тест 15: Закрывающие скобки в неправильном порядке"""
        self.assertFalse(Solution().isValid("([)]"))

    def test_extra_opening(self):
        """Тест 16: Лишняя открывающая скобка"""
        self.assertFalse(Solution().isValid("()("))

    def test_extra_closing(self):
        """Тест 17: Лишняя закрывающая скобка"""
        self.assertFalse(Solution().isValid("())"))

    def test_invalid_characters(self):
        """Тест 18: Недопустимые символы"""
        self.assertFalse(Solution().isValid("(a)"))

    def test_mixed_brackets_fail(self):
        """Тест 19: Смешанные скобки с ошибкой"""
        self.assertFalse(Solution().isValid("{[(])}"))

    def test_alternating_brackets(self):
        """Тест 20: Чередующиеся скобки"""
        self.assertFalse(Solution().isValid("{()}[(])"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
