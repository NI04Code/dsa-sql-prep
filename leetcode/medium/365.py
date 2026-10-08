# https://leetcode.com/problems/water-and-jug-problem

from collections import deque
import math

class Solution:
    def canMeasureWaterBFS(self, x: int, y: int, target: int) -> bool:
        queue = deque()
        queue.append((0, 0))
        visited = []
        
        while len(queue) > 0:
            a, b = queue.popleft()
            visited.append((a, b))
            if a + b == target:
                return True
            
            if a == 0 and b == 0:
                if (x, b) not in visited:
                    queue.append((x, b))
                if (a, y) not in visited:
                    queue.append((a, y))
            if a > 0 and b == 0:
                if (a, y) not in visited:
                    queue.append((a, y))
                if (x, b) not in visited:
                    queue.append((x, b))
                
                fill_b = min(a,y)
                remain_a = max(0, a - min(a,y))
                if (remain_a, fill_b) not in visited:
                    queue.append((remain_a, fill_b))
            
            if a == 0 and b > 0:
                if (a, y) not in visited:
                    queue.append((a, y))
                if (x, b) not in visited:
                    queue.append((x, b))
                
                fill_a = min(b,x)
                remain_b = max(0, b - min(b,x))
                if (fill_a, remain_b) not in visited:
                    queue.append((fill_a, remain_b))
            
            if a > 0 and b > 0:
                if (0, b) not in visited:
                    queue.append((0,b))
                if (a, 0) not in visited:
                    queue.append((a,0))
                if (x, b) not in visited:
                    queue.append((x,b))
                if (a, y) not in visited:
                    queue.append((a,y))
                
                fill_b = min(y, a+b)
                remain_a = a - abs(b - fill_b)
                if (remain_a, fill_b) not in visited:
                    queue.append((remain_a, fill_b))
                
                fill_a = min(x, a+b)
                remain_b = b - abs(a - fill_a)
                if (fill_a, remain_b) not in visited:
                    queue.append((fill_a, remain_b))


        return False

    def canMeasureWaterBFSRefined(self, x: int, y: int, target: int) -> bool:
            if target > x + y:
                return False
                
            queue = deque([(0, 0)])
            visited = {(0, 0)}

            while queue:
                a, b = queue.popleft()
                
                if a + b == target:
                    return True

                # All possible valid next moves
                next_states = [
                    (x, b),  # Fill jug x
                    (a, y),  # Fill jug y
                    (0, b),  # Empty jug x
                    (a, 0),  # Empty jug y
                    # Pour x into y
                    (max(0, a - (y - b)), min(y, a + b)),
                    # Pour y into x
                    (min(x, a + b), max(0, b - (x - a)))
                ]

                for state in next_states:
                    if state not in visited:
                        visited.add(state)
                        queue.append(state)

            return False

    
    def canMeasureWaterBezout(self, x: int, y: int, target: int) -> bool:
        '''
        There are only two rules to check:
        1. The target cannot exceed the total capacity of both jugs combined (target <= x + y).
        2. The target must be divisible by gcd(x, y), or target == 0.
        '''

        if target > x+y:
            return False
        if target == 0:
            return True

        return target % math.gcd(x, y) == 0
    
            