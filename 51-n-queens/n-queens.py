class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        cols = set()
        dia1 = set()
        dia2 = set()
        res = []
        def dfs(r):
            if r == n:
                solution = [''.join(row) for row in board]
                res.append(solution)
                return 

            for c in range(n):
                if c in cols or r + c in dia1 or r - c in dia2:
                    continue

                cols.add(c)
                dia1.add(r + c)
                dia2.add(r - c)
                board[r][c] = 'Q'

                dfs(r + 1)

                cols.remove(c)
                dia1.remove(r + c)
                dia2.remove(r - c)
                board[r][c] = '.'

        dfs(0)
        return res
