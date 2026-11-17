# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters
from collections import defaultdict

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        n = len(s)
        maxLen = 0
        for allowedUnique in range(1, 27):
            count = defaultdict(int)
            uniqueChar = 0
            uniqueCharWithKCount = 0
        
            left = 0
            for right in range(n):
                char = s[right]
                if count[char] == 0:
                    uniqueChar += 1

                count[char] += 1
                if count[char] == k:
                    uniqueCharWithKCount += 1

                while uniqueChar > allowedUnique:
                    leftChar = s[left]
                    count[leftChar] -= 1
                    
                    if count[leftChar] < k and count[leftChar] + 1 == k:
                        uniqueCharWithKCount -= 1
                    if count[leftChar] == 0:
                        uniqueChar -= 1
                    
                    left += 1

                if uniqueCharWithKCount == allowedUnique:
                    maxLen = max(maxLen, right - left + 1)
                
        return maxLen