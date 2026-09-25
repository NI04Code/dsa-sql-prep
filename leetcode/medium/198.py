# https://leetcode.com/problems/house-robber/
class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2, n):
            for j in range(0, i-1):
                dp[i] = max(dp[i], dp[j] + nums[i])

        return max(dp[n-1], dp[n-2])

# Imagine the dp is to cache how much money we can get in position i
# its either i-1 is better or current i is better
class SolutionOptimal:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[n-1]

