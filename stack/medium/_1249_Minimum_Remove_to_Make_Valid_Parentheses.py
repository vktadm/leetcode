class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        total_opens = 0
        balance = 0
        char_list = []

        for char in s:
            if char == "(":
                total_opens += 1
                balance += 1
            elif char == ")":
                if balance == 0:
                    continue
                balance -= 1
            char_list.append(char)

        opens_to_keep = total_opens - balance
        result = []

        for char in char_list:
            if char == "(":
                opens_to_keep -= 1
                if opens_to_keep < 0:
                    continue
            result.append(char)

        return "".join(result)


if __name__ == "__main__":
    print(Solution().minRemoveToMakeValid("))(("))
