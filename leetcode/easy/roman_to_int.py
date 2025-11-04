# https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0

        i = 0
        while i < len(s) - 1:
            if s[i] == "I":
                if s[i + 1] == "V" or s[i + 1] == "X":
                    count -= 1
                else:
                    count += 1
            elif s[i] == "V":
                count += 5
            elif s[i] == "X":
                if s[i + 1] == "L" or s[i + 1] == "C":
                    count -= 10
                else:
                    count += 10
            elif s[i] == "L":
                count += 50
            elif s[i] == "C":
                if s[i + 1] == "D" or s[i + 1] == "M":
                    count -= 100
                else:
                    count += 100
            elif s[i] == "D":
                count += 500
            elif s[i] == "M":
                count += 1000
           
            i += 1
        
        
        if s[len(s) - 1] == "I":
            count += 1
        elif s[i] == "V":
            count += 5
        elif s[i] == "X":
            count += 10
        elif s[i] == "L":
            count += 50
        elif s[i] == "C":
            count += 100
        elif s[i] == "D":
            count += 500
        elif s[i] == "M":
            count += 1000
        
        return count