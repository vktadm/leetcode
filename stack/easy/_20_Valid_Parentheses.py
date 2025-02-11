class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        p_map = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        p_stack = []

        for value in s:
            if p_stack and value in p_map:
                pre_value = p_stack.pop()
                if pre_value != p_map[value]:
                    return False
            else:
                p_stack.append(value)

        if len(p_stack):
            return False
        return True
