class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(i, j):
            if not 0 <= i < m or not 0 <= j < n:
                return
            if grid[i][j] != '1':
                return
            grid[i][j] = '#'
            dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for a, b in dir:
                dfs(i + a, j + b)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        
        return res
        