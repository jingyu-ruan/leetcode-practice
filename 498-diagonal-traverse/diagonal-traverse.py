class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        m, n = len(mat), len(mat[0]) # row col
        i, j = 0, 0
        up = True
        for k in range(m * n):
            res.append(mat[i][j])
            if up:
                if i > 0 and j < n - 1:
                    i -= 1
                    j += 1
                else:
                    up = False
                    if j == n - 1:
                        i += 1
                    elif i == 0:
                        j += 1
                    
            else: # going down
                if i < m - 1 and j > 0:
                    i += 1
                    j -= 1
                else:
                    up = True
                    if i == m - 1:
                        j += 1
                    elif j == 0:
                        i += 1
                    
        
        return res
