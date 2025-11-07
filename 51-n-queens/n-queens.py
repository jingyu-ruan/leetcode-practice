class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        diag1 = set()
        diag2 = set()
        board = [['.'] * n for _ in range(n)]

        def bt(row):
            if row == n:
                to_append = []
                for r in board:
                    to_append.append(''.join(r))
                res.append(to_append)
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (col + row) in diag2:
                    continue

                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(col + row)

                bt(row + 1)

                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(col + row)

        bt(0)

        return res
