# https://leetcode.com/problems/zigzag-conversion
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        m = [[] for _ in range(numRows)]

        i = 0
        counter = 0
        zig = 1
        while i < len(s):
            if counter == numRows:
                index = counter - 1
                m[index-zig].append(s[i])
               
                if (index-zig) == 0:
                    zig = 1
                    counter = 1
                else:
                    zig += 1

            else:
                m[counter].append(s[i])
                counter += 1
            
            i += 1
        
        output = ""
        for row in m:
           output += "".join(row)
        
        return output