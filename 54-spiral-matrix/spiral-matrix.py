class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []
        top, bottom = 0, m - 1
        left, right = 0, n - 1

        while top <= bottom and left <= right:
            # 从左到右
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1

            # 从上到下
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1

            # 检查边界是否交叉
            if top > bottom or left > right:
                break

            # 从右到左
            for c in range(right, left - 1, -1):
                res.append(matrix[bottom][c])
            bottom -= 1

            # 从下到上
            for r in range(bottom, top - 1, -1):
                res.append(matrix[r][left])
            left += 1

        return res
    
