# https://leetcode.com/problems/counting-bits

class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n+1)
        for i in range(len(dp)):
            dp[i] = dp[i >> 1] + (i & 1)
        
        return dp
        