# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip().split()
        last_word = s[len(s) - 1]
        
        return len(last_word)
        