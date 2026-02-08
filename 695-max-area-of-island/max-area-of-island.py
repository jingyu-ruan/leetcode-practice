class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        def dfs(i, j):
            nonlocal res
            if not 0 <= i < m or not 0 <= j < n:
                return 0
            if grid[i][j] != 1:
                return 0
            grid[i][j] = '#'
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)
            up = dfs(i - 1, j)
            down = dfs(i + 1, j)

            return left + right + up + down + 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        
        return res