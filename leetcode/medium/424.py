# https://leetcode.com/problems/longest-repeating-character-replacement

from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCounts = defaultdict(int)
        left = 0
        maxFreq = 0
        maxLen = 0
        for right in range(len(s)):
            charCounts[s[right]] += 1
            maxFreq = max(maxFreq, charCounts[s[right]])
            
            while (right - left + 1) - maxFreq > k:
                charCounts[s[left]] -= 1
                left += 1
            
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen





        