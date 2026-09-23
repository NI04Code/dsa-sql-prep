# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i
class Solution:
    def kthCharacter(self, k):
        word = "a"
        for i in range(k):
            next_char = ""
            for w in word:
                if w == "z":
                    next_char += "a"
                else:
                    next_char += chr(ord(w) + 1)
            
            word += next_char
            if len(word) >= k:
                break
        
        return word[k-1]
        