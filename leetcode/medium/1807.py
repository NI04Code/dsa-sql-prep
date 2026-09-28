# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledgeDict = {k: v for k, v in knowledge}

        res = ""
        
        i = 0
        while i < len(s):
            if s[i] == "(":
                j = s.find(")", i)
                key = s[i+1:j]
                res += knowledgeDict.get(key, "?")

                i = j + 1
            else:
                res += s[i]
                i += 1

               
        
        return res
        