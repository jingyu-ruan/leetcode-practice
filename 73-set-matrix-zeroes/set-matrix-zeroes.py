class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        stack = []
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    stack.append((i, j))
        
        while stack:
            r, c = stack.pop()
            for i in range(n):
                matrix[r][i] = 0
            for j in range(m):
                matrix[j][c] = 0    