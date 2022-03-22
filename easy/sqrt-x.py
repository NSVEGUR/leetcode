class Solution:
    def mySqrt(self, x: int) -> int:
        s = 0
        e = x
        ans = 0
        mid = (s+e)//2
        while s <= e:
            t = mid*mid
            if t == x:
                return mid
            elif t < x:
                ans = mid
                s = mid + 1
            elif t > x:
                e = mid - 1
            mid = (s+e)//2
        return ans


sol = Solution()
print(sol.mySqrt(16))
