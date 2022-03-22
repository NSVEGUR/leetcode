from typing import List
import sys


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = - sys.maxsize - 1
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            maxi = max(maxi, sum)
            if sum < 0:
                sum = 0
        return maxi


sol = Solution()
print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
