class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        1 4 7
        2 5 8
        3 6 9
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        l, r = 0, n - 1
        while l < r:
            for i in range(m):
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
            l += 1
            r -= 1
        
        