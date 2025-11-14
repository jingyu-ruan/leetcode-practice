class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0

        def dfs(r, c):
            if grid[r][c] != '1':
                return 

            if grid[r][c] == '1':
                grid[r][c] = '#'            
            if r - 1 >= 0:
                dfs(r - 1, c)
            if r + 1 < m:
                dfs(r + 1, c)
            if c - 1 >= 0:
                dfs(r, c - 1)
            if c + 1 < n:
                dfs(r, c + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1

        return res
            



