# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        strx = str(x)

        i = 0
        while i < len(strx):
            if strx[i] != strx[len(strx)-i-1]:
                return False
            
            if i >= len(strx)-i-1:
                return True

            i += 1