class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        def dfs(r, c, visited):
            visited[r][c] = True

            directions = [[1, 0], [0,1], [-1, 0], [0, -1]]
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if visited[nr][nc]:
                    continue
                if heights[nr][nc] < heights[r][c]:
                    continue
                
                dfs(nr, nc, visited)

        for c in range(n):
            dfs(0, c, pacific)
            dfs(m - 1, c, atlantic)

        for r in range(m):
            dfs(r, 0, pacific)
            dfs(r, n - 1, atlantic)

        res = []
        for r in range(m):
            for c in range(n):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r, c])

        return res