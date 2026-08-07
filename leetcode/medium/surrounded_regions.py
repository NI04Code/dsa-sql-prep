# https://leetcode.com/problems/surrounded-regions

from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        h, w = len(board), len(board[0])

        for i in range(w):
            if board[0][i] == "O":
                self.bfs(board, 0, i)
            
            if board[h-1][i] == "O":
                self.bfs(board, h-1, i)
        
        for i in range(h):
            if board[i][0] == "O":
                self.bfs(board, i, 0)
            
            if board[i][w-1] == "O":
                self.bfs(board, i, w-1)

        for i in range(h):
            for j in range(w):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "#":
                    board[i][j] = "O"
    
    def bfs(self, board, r, c):
        h, w = len(board), len(board[0])

        queue = deque([(r,c)])
        board[r][c] = "#"

        while queue:
            r, c = queue.popleft()

            if c < w-1 and board[r][c+1] == "O":
                board[r][c+1] = "#"
                queue.append((r,c+1))
            if c > 0 and board[r][c-1] == "O":
                board[r][c-1] = "#"
                queue.append((r,c-1))
            if r < h-1 and board[r+1][c] == "O":
                board[r+1][c] = "#"
                queue.append((r+1,c))
            if r > 0 and board[r-1][c] == "O":
                board[r-1][c] = "#"
                queue.append((r-1,c))
