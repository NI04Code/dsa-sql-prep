# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        start = 0
        maxLen = 1
        for i in range(n):
            dp[i][i] = True
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                maxLen = 2
                start = i
        
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if j - i + 1 > maxLen:
                        maxLen = j - i + 1
                        start = i
        
        return s[start:start + maxLen]