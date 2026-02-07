class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(path, i):
            if sum(path) > target:
                return
            if sum(path) == target:
                res.append(path[:])
            
            for j in range(i, len(candidates)):
                dfs(path + [candidates[j]], j)
        
        dfs([], 0)
        return res