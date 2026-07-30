# https://leetcode.com/problems/set-matrix-zeroes/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r, c = len(matrix), len(matrix[0])
        ls = []
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    ls.append((i,j))
        
        for a, b in ls:
            matrix[a] = [0] * c
            for row in matrix:
                row[b] = 0


        