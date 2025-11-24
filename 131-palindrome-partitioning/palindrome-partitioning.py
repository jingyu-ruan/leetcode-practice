class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palin(x):
            l = 0
            r = len(x) - 1
            while l <= r:
                if x[l] != x[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        res = []
        path = []
        n = len(s)
        def dfs(start):
            if start == n:
                res.append(path[:])
                return
            for j in range(start, n):
                if not is_palin(s[start:j + 1]):
                    continue
                path.append(s[start:j + 1])
                dfs(j + 1)
                path.pop()


        dfs(0)
        return res