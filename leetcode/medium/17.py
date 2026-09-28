# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        digitToLetter = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        }

        res = []

        def combineChar(index, str):
            if index == len(digits):
                res.append(str)
                return
            
            currDigit = digits[index]

            for char in digitToLetter[currDigit]:
                combineChar(index + 1, str + char)
        
        combineChar(0, "")

        return res