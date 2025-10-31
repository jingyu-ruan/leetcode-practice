import copy
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix2 = copy.deepcopy(matrix)
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix2[i][j] == 0:
                    for col in range(n):
                        matrix[i][col] = 0
                    for row in range(m):
                        matrix[row][j] = 0