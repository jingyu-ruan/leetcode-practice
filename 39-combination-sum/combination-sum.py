class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        def dfs(path, need, start):
            for i in range(start, n):
                if need == 0:
                    res.append(path[:])
                    return
                if need < 0:
                    return
                
                dfs(path + [candidates[i]], need - candidates[i], i)
        
        dfs([], target, 0)
        return res