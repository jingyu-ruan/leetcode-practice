class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for r in range(m):
            if matrix[r][0] == target:
                return True
            if matrix[r][0] > target:
                continue
            if matrix[r][0] < target:
                for c in range(n):
                    if matrix[r][c] > target:
                        continue
                    if matrix[r][c] == target:
                        return True

        return False    
