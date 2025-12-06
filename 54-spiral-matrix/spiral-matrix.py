class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top, down = 0, m - 1
        left, right = 0, n - 1
        res = []
        nums = 0
        while top <= down and left <= right:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
                nums += 1
            if nums == m * n:
                break
            top += 1

            for i in range(top, down + 1):
                res.append(matrix[i][right])
                nums += 1
            if nums == m * n:
                break
            
            right -= 1

            for i in range(right, left - 1, -1):
                res.append(matrix[down][i])
                nums += 1
            if nums == m * n:
                break

            down -= 1

            for i in range(down, top - 1, -1):
                res.append(matrix[i][left])
                nums += 1
            if nums == m * n:
                break
            
            left += 1

        return res