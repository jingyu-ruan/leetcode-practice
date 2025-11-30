class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        dia1 = set()
        dia2 = set()
        res = []
        path = []
        queens = []
        def dfs(i):
            # base case
            if i == n:
                queens.append(path[:])
                return

            for j in range(n):
                if j not in cols and i + j not in dia1 and i - j not in dia2:
                    cols.add(j)
                    dia1.add(i + j)
                    dia2.add(i - j)
                    path.append((i, j))
                    dfs(i + 1)
                    cols.remove(j)
                    dia1.remove(i + j)
                    dia2.remove(i - j)
                    path.pop()
        
        dfs(0)

        for pos in queens:
            board = [['.'] * n for _ in range(n)]
            for i, j in pos:
                board[i][j] = 'Q'
            upload = []
            for row in board:
                upload.append(''.join(row))
            res.append(upload)

        return res
