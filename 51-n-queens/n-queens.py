class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        dia1 = set()
        dia2 = set()
        board = [['.'] * n for _ in range(n)]
        path = []
        self.to_append = []
        res = []
        def dfs(r):
            if r == n:
                solution = []
                for row in board:
                    solution.append(''.join(row))
                res.append(solution)
                return 
            
            for c in range(n):
                if c in cols or c + r in dia1 or c - r in dia2:
                    continue
                cols.add(c)
                dia1.add(c + r)
                dia2.add(c - r)
                board[r][c] = 'Q'

                dfs(r + 1)

                cols.remove(c)
                dia1.remove(c + r)
                dia2.remove(c - r)
                board[r][c] = '.'
    
        dfs(0)
        return res