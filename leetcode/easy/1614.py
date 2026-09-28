# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses

from collections import deque

class Solution:
    def maxDepth(self, s: str) -> int:
        stack = deque()
        
        depth = 0
        for c in s:
            if c == "(":
                stack.append("(")
            if c == ")":
                stack.pop()
            
            depth = max(depth, len(stack))

        return depth