# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_string = ""
        longest = 0
        count = 0
        for i in range(0, len(s)):
            if s[i] not in current_string:
                current_string += s[i]
                count += 1
            else:
                if count > longest:
                    longest = count
                
                current_string = "" + s[i]
                count = 1
                for j in range(i-1, -1, -1):
                    if s[j] == s[i]:
                        break
                    count += 1
                    current_string = s[j] + current_string


        
        if count > longest:
            longest = count
        
        return longest
        