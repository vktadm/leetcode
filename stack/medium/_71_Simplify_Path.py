import unittest


class Solution:
    def simplifyPath(self, path: str) -> str:
        l = []
        path = path.split("/")
        for i in path:
            if i == "":
                continue
            elif i == "..":
                if l:
                    l.pop()
            elif i == ".":
                continue
            else:
                l.append(i)

        return "/" + "/".join(l)


class SolutionTest(unittest.TestCase):
    def test_1(self):
        path = "/.../a/../b/c/../d/./"
        result = "/.../b/d"
        actual = Solution().simplifyPath(path)
        assert actual == result
