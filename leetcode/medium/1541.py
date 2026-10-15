# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string

from collections import deque

class Solution:
    def minInsertions(self, s: str) -> int:
        result = 0
        stack = deque()
        
        i = 0; n = len(s)
        while i < n:
            if s[i] == '(':
                stack.append('(')
                i += 1
            else:
                if i < n-1 and s[i:i+2] == '))':
                    if not stack:
                        result += 1
                    else:
                        stack.popleft()
                    i += 2
                
                elif s[i] == ')':
                    result += 1
                    if not stack:
                        result += 1
                    else:
                        stack.popleft()

                    i += 1
        
        result += 2*len(stack)

        return result  