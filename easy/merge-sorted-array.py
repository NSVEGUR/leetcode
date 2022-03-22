from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        def filterArray(nums: List[int], n):
            if len(nums) > n:
                for i in range(len(nums)-n):
                    nums.pop()
            return nums

        def smallest(nums1, nums2):
            if len(nums1) > len(nums2):
                return (nums2, nums1)
            return (nums1, nums2)

        j = 0
        i = 0

        nums1 = filterArray(nums1, m)
        nums2 = filterArray(nums2, n)

        (nums1, nums2) = smallest(nums1, nums2)
        for i in range(len(nums1)):
            while j < len(nums2) and nums2[j] <= nums1[i]:
                nums1.insert(i, nums2[j])
                i += 1
                j += 1
        while j < len(nums2):
            nums1.append(nums2[j])
            j += 1
        return nums1


sol = Solution()
print(sol.merge([1, 2, 4, 5, 6, 0], 5, [3], 1))
