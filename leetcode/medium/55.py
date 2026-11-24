# https://leetcode.com/problems/jump-game
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        
        for i in range(1, n):
            if dp[i - 1] < i:
                return False
            dp[i] = max(dp[i - 1], i + nums[i])
            
        return True