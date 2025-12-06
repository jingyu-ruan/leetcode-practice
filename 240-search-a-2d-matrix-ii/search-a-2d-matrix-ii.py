class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        while i < len(matrix) and matrix[i][0] <= target:
            j = 0
            while j < len(matrix[0]) and matrix[i][j] <= target:
                if matrix[i][j] == target:
                    return True
                j += 1
            i += 1
        
        return False