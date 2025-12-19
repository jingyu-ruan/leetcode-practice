class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palin(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        res = []
        n = len(s)
        def dfs(path, start):
            if start == n:
                res.append(path[:])
                return
            
            for i in range(start, n):
                if is_palin(start, i):
                    dfs(path + [s[start:i+1]], i + 1)
        
        dfs([], 0)
        return res