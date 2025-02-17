import unittest

from _104_Maximum_Depth_of_Binary_Tree import Solution, TreeNode


class SolutionTest(unittest.TestCase):

    def run_test(self, result, root):
        s = Solution()
        self.assertEqual(result, s.maxDepth(root))

    def test_case_1(self):
        nodes = [3, 9, 20, None, None, 15, 7]
        root = TreeNode(3)

        node1 = TreeNode(9)
        node2 = TreeNode(20)

        node4 = TreeNode(15)
        node5 = TreeNode(7)

        root.left = node1
        root.right = node2

        node2.right = node4
        node2.left = node5

        self.run_test(3, root)

    def test_case_2(self):
        nodes = [1, None, 2]
        root = TreeNode(3)

        node1 = TreeNode(2)

        root.right = node1

        self.run_test(2, root)

    def test_case_3(self):
        nodes = [10]
        root = TreeNode(10)
        self.run_test(1, root)

    def test_case_4(self):
        nodes = []
        root = None
        self.run_test(0, root)


if __name__ == "__main__":
    unittest.main()
