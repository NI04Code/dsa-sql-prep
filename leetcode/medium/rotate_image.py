# https://leetcode.com/problems/rotate-image/
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        s = len(matrix)

        for i in range(s):
            for j in range(i+1, s):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
            matrix[i] = matrix[i][::-1]
            