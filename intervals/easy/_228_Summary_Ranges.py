class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result_lst = []
        prev_idx = 0
        idx = 1

        while idx <= len(nums):
            if idx == len(nums) or ((nums[idx] - nums[prev_idx]) != (idx - prev_idx)):
                if (idx - prev_idx) == 1:
                    result_lst.append(f'{nums[prev_idx]}')
                else:
                    result_lst.append(f'{nums[prev_idx]}->{nums[idx - 1]}')
                prev_idx = idx
            idx += 1

        return result_lst
