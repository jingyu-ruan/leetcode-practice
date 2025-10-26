class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        down = m-1
        left = 0
        right = n-1

        while top <= down and left <= right:
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1
            if top > down:
                break
            
            for r in range(top, down + 1):
                res.append(matrix[r][right])
            right -= 1
            if left > right:
                break

            for c in range(right, left - 1, -1):
                res.append(matrix[down][c])
            down -= 1
            if top > down:
                break

            for r in range(down, top - 1, -1):
                res.append(matrix[r][left])
            left += 1
            if left > right:
                break

        return res



            

        return res