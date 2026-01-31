from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    q.append((i, j))
                    res += 1
                    grid[i][j] = '#'
                    while q:
                        r, c = q.popleft()
                        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                        for a, b in dir:
                            if 0 <= r + a < m and 0 <= c + b < n and grid[r+a][c+b] == '1':
                                q.append((r + a, c + b))
                                grid[r + a][c + b] = '#'
        return res


        