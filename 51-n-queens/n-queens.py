class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag1 = set()
        diag2 = set()
        board = [['.'] * n for _ in range(n)]
        res = []
        queens = []

        def dfs(r):
            if r == n:
                for a, b in queens:
                    nonlocal board
                    board[a][b] = 'Q'
                m = []
                for row in board:
                    m.append(''.join(row))
                res.append(m)
                board = [['.'] * n for _ in range(n)]
                return
            
            for c in range(n):
                if c not in cols and r + c not in diag1 and r - c not in diag2:
                    cols.add(c)
                    diag1.add(r + c)
                    diag2.add(r - c)
                    queens.append((r, c))

                    dfs(r + 1)

                    cols.remove(c)
                    diag1.remove(r + c)
                    diag2.remove(r - c)
                    queens.pop()
        
        dfs(0)
        return res