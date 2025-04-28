from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        for i in nums:
            if max_jump < 0:
                return False

            elif max_jump < i:
                max_jump = i
            max_jump -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    print("---Test 1---")
    nums = [2, 3, 1, 1, 4]
    print(s.canJump(nums))
    print("---Test 2---")
    nums = [3, 2, 1, 0, 4]
    print(s.canJump(nums))
