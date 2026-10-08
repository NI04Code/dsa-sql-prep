# https://leetcode.com/problems/perfect-squares

import math

class Solution:
    def numSquares(self, n: int) -> int:
        def getPerfectSquare(n):
            max_i = math.isqrt(n)
            return [i**2 for i in range(1, max_i+1)]
        
        psList = getPerfectSquare(n)
        dp = [n+1 for _ in range(n+1)]
        dp[0] = 0
        
        for i in range(1, n+1):
            for ps in psList:
                if ps <= i:
                    dp[i] = min(dp[i], dp[i-ps] + 1)
        
        return dp[n]
