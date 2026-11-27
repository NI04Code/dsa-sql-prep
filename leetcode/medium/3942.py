# https://leetcode.com/problems/maximum-number-of-items-from-sale-i

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        bonus = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    bonus[i] += 1

        dp = [-1] * (budget + 1)
        dp[0] = 0
        for i, (_, p) in enumerate(items):
            for cap in range(budget, p - 1, -1):
                if dp[cap - p] != -1:
                    dp[cap] = max(dp[cap], dp[cap - p] + 1 + bonus[i])

        min_p = min(p for _, p in items)
        
        return max(
            dp[cap] + (budget - cap) // min_p
            for cap in range(budget + 1)
            if dp[cap] != -1
        )