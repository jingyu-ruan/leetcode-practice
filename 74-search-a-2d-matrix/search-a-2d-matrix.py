class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        layout = []
        for i in range(0, len(matrix)):
            layout.extend(matrix[i])

        l, r = 0, len(layout) - 1
        while l <= r:
            m = (l + r) // 2
            if layout[m] == target:
                return True
            elif layout[m] > target:
                r = m - 1
            else:
                l = m + 1

        return False