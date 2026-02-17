class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        num_set = set()
        res = []
        def dfs(path, i):
            nonlocal res
            if sum(path) == target:
                res.append(path[:])
                return
            if sum(path) > target:
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1] and j - 1 not in num_set:
                    continue
                num_set.add(j)
                dfs(path + [candidates[j]], j + 1)
                num_set.remove(j)
        
        dfs([], 0)
        return res