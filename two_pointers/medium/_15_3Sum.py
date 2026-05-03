class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

                elif total > 0:
                    k -= 1
                elif total < 0:
                    j += 1

        return result


if __name__ == "__main__":
    s = Solution()
    height = [-1, 0, 1, 2, -1, -4]
    print(s.threeSum(height))
    height = [0, 1, 1]
    print(s.threeSum(height))
    height = [0, 0, 0]
    print(s.threeSum(height))
