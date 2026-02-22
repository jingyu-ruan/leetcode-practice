class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        v = 1
        left, right = 0, n - 1
        up, down = 0, n - 1
        while True:
            for i in range(left, right + 1):
                res[up][i] = v
                v += 1
            up += 1
            if v == n * n + 1:
                return res
            
            for i in range(up, down + 1):
                res[i][right] = v
                v += 1
            right -= 1
            if v == n * n + 1:
                return res

            for i in range(right, left - 1, -1):
                res[down][i] = v
                v += 1
            down -= 1
            if v == n * n + 1:
                return res

            for i in range(down, up - 1, -1):
                res[i][left] = v
                v += 1
            left += 1
            if v == n * n + 1:
                return res