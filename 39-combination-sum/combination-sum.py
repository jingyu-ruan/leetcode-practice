class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def dfs(start, remain):
            if remain == 0:
                res.append(path.copy())
                return
            
            if remain < 0:
                return

            for i in range(start, len(candidates)):
                x = candidates[i]

                if x > remain:
                    break
                
                path.append(x)
                dfs(i, remain - x)
                path.pop()

        dfs(0, target)
        return res