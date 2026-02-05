# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        try:
            for c in s:
                if c == ")":
                    popped = stk.pop()
                    if popped != "(":
                        return False
                elif c == "]":
                    popped = stk.pop()
                    if popped != "[":
                        return False
                elif c == "}":
                    popped = stk.pop()
                    if popped != "{":
                        return False
                else:
                    stk.append(c)
        except IndexError:
            return False

        if len(stk) > 0:
            return False
        
        return True
        