
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(x):
            if len(path) == k:
                res.append(path[:])
                return
            
            for num in range(x, n + 1):
                path.append(num)
                dfs(num + 1)
                path.pop()

        
        dfs(1)
        
        return res