class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def dfs(lst, i):
            new = lst + [i]
            if len(new) == k:
                res.append(new)
                return

            for a in range(i + 1, n + 1):
                dfs(new, a)

        for i in range(1, n + 1):
            dfs([], i)
        
        return res