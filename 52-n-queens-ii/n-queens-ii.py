class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        dia1 = set()
        dia2 = set()
        res = 0
        def dfs(r):
            if r == n:
                nonlocal res
                res += 1
                return
            
            for c in range(n):
                if c not in cols and r + c not in dia1 and r - c not in dia2:
                    cols.add(c)
                    dia1.add(r + c)
                    dia2.add(r - c)

                    dfs(r + 1)

                    cols.remove(c)
                    dia1.remove(r + c)
                    dia2.remove(r - c)
        
        dfs(0)

        return res