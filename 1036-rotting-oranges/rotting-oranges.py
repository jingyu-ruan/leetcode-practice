from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        flatten = []
        for lst in grid:
            flatten.extend(lst)
        if 2 not in flatten and 1 not in flatten:
            return 0
        if 2 in flatten and 1 not in flatten:
            return 0
        if 2 not in flatten:
            return -1
        m = len(grid)
        n = len(grid[0])
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
        res = 0
        while queue:
            cur_len = len(queue)
            for _ in range(cur_len):
                i, j = queue.popleft()
                dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for a, b in dir:
                    if 0 <= i + a < m and 0 <= j + b < n and grid[i+a][j+b] == 1:
                        grid[i+a][j+b] = 2
                        queue.append((i+a, j+b))
            res += 1

        flatten = []
        for lst in grid:
            flatten.extend(lst)
        if 1 in flatten:
            return -1

        return res - 1