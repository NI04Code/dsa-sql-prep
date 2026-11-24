# https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [n] * n
        dp[0] = 0
        
        for i in range(n):
            for num in range(1, nums[i]+1):
                if i+num < n:
                    dp[i+num] = min(dp[i+num], dp[i]+1)
        
        return dp[n-1]
        