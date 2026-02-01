class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        up, down = 0, m - 1
        left, right = 0, n - 1
        res = []
        cur = 0
        while True:
            for i in range(left, right + 1):
                res.append(matrix[up][i])
                cur += 1
            up += 1
            if cur == m * n:
                return res

            for i in range(up, down + 1):
                res.append(matrix[i][right])
                cur += 1
            right -= 1
            if cur == m * n:
                return res

            for i in range(right, left - 1, -1):
                res.append(matrix[down][i])
                cur += 1
            down -= 1
           
            if cur == m * n:
                return res
            
            for i in range(down, up - 1, -1):
                res.append(matrix[i][left])
                cur += 1
            left += 1
            if cur == m * n:
                return res
            
        return res