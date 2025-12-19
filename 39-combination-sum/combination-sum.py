class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        def dfs(path, need, i):
            if need == 0:
                res.append(path[:])
                return
            if need < 0:
                return
            
            for j in range(i, n):
                dfs(path + [candidates[j]], need - candidates[j], j)
            
        for k in range(n):
            dfs([candidates[k]], target - candidates[k], k)
        
        return res