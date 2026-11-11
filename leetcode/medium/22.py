# https://leetcode.com/problems/generate-parentheses
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        dp = [[] for _ in range(n+1)]
        dp[0] = [""]
        
        for i in range(1, n+1):
            for j in range(i):
                for a in dp[j]:
                    for b in dp[i - 1 - j]:
                        dp[i].append(f"({a}){b}")

        return dp[n]