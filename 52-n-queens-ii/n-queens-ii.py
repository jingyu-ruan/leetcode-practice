class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        dia1 = set()
        dia2 = set()
        self.res = 0

        def dfs(r):
            if r == n:
                self.res += 1
                return
            
            for c in range(n):
                if c in cols or c + r in dia1 or r - c in dia2:
                    continue
                cols.add(c)
                dia1.add(c + r)
                dia2.add(r - c)

                dfs(r + 1)

                cols.remove(c)
                dia1.remove(c + r)
                dia2.remove(r - c)

        dfs(0)
        return self.res
