class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        path = []
        def dfs(idx, need):
            if need == 0:
                res.append(path[:])
                return
            if need < 0:
                return 
            for i in range(idx, n):
                path.append(candidates[i])
                dfs(i, need - candidates[i])
                path.pop()

        dfs(0, target)

        return res