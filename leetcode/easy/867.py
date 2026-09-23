# https://leetcode.com/problems/transpose-matrix

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        height = len(matrix)
        width = len(matrix[0])

        transpose_m = [[0] * height for _ in range(width)]
        for i in range(height):
            for j in range(width):
               transpose_m[j][i] = matrix[i][j]
        
        return transpose_m