class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        n = len(candidates)
        def dfs(t, idx):
            if sum(path) == t:
                res.append(path[:])
                return
            if sum(path) > t: 
                return
            for i in range(idx, n):
                path.append(candidates[i])
                dfs(t, i)
                path.pop()
        
        
        dfs(target, 0)
        
        return res
            

