from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        l = len(nums)
        i = 0
        while i < l:
            if nums[i] == '_':
                i += 1
            elif nums[i] in nums[0:i]:
                nums.pop(i)
                nums.append('_')
                i -= 1
            else:
                i += 1
                count += 1
        count = 0
        for n in nums:
            if n != '_':
                count += 1
        return count
