class Solution:
    def climbStairs(self, n: int) -> int:
        def ways(n, dp):
            if n < 3:
                return n
            if n in dp:
                return dp[n]
            dp[n] = ways(n-1, dp) + ways(n-2, dp)
            return dp[n]
        return ways(n, {})
