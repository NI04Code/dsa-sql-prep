# https://leetcode.com/problems/integer-to-roman

class Solution:
    def intToRoman(self, num: int) -> str:
        x = num
        output = ""
        while x != 0:
            if x - (x % 1000) != 0:
                s = x - (x % 1000)
                output += "M" * (s//1000)
                x = x % 1000
            elif x - (x % 100) != 0:
                s = x - (x % 100)
                if s < 500:
                    if s == 400:
                        output += "CD"
                    else:
                        output += "C" * (s//100)
                else:
                    if s == 900:
                        output += "CM"
                    else:
                        output += "D" + "C" * ((s-500)//100)
                x = x % 100
            elif x - (x % 10) != 0:
                s = x - (x % 10)
                if s < 50:
                    if s == 40:
                        output += "XL"
                    else:
                        output += "X" * (s//10)
                else:
                    if s == 90:
                        output += "XC"
                    else:
                        output += "L" + "X" * ((s-50)//10)
                x = x % 10
            else:
                if x < 5:
                    if x == 4:
                        output += "IV"
                    else:
                        output += "I" * x
                else:
                    if x == 9:
                        output += "IX"
                    else:
                        output += "V" + "I" * (x-5)
                
                x = 0
        
        return output