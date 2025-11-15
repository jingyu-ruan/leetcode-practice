from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        flatten = []

        for i in range(len(grid)):
            flatten.extend(grid[i])
        if 1 not in flatten:
            return 0
        if 2 not in flatten:
            return -1
        
        queue = deque()
        m = len(grid)
        n = len(grid[0])
        res = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        while queue:
            cur_orgs = len(queue)
            for o in range(cur_orgs):
                cur = queue.popleft()
                a, b = cur[0], cur[1]
                if a - 1 >= 0 and grid[a-1][b] == 1:
                    queue.append((a-1, b))
                    grid[a-1][b] = 2
                if a + 1 < m and grid[a+1][b] == 1:
                    queue.append((a+1, b))
                    grid[a+1][b] = 2
                if b - 1 >= 0 and grid[a][b-1] == 1:
                    queue.append((a, b-1))
                    grid[a][b-1] = 2
                if b + 1 < n and grid[a][b+1] == 1:
                    queue.append((a, b+1))
                    grid[a][b+1] = 2
            res += 1

        for f in range(m):
            if 1 in grid[f]:
                return -1
        return res - 1