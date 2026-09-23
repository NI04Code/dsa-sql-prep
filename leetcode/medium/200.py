# https://leetcode.com/problems/number-of-islands/

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        queue = deque()
        count = 0
        for i in range(m):
            for j in range(n):
                if  grid[i][j] == "1":
                    queue.append((i,j))
                    grid[i][j] = "0"
                    
                    while queue:
                        r, c = queue.popleft()
                        
                        if r != 0 and grid[r-1][c] == "1":
                            queue.append((r-1,c))
                            grid[r-1][c] = "0"
                        
                        if r != m-1 and grid[r+1][c] == "1":
                            queue.append((r+1,c))
                            grid[r+1][c] = "0"
                        
                        if c != 0 and grid[r][c-1] == "1":
                            queue.append((r,c-1))
                            grid[r][c-1] = "0"

                        if c != n-1 and grid[r][c+1] == "1":
                            queue.append((r,c+1))
                            grid[r][c+1] = "0"
                    
                    count += 1
        
        return count


        