class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(path, n, i):
            res.append(path[:])
            if n == len(nums):
                return
            for j in range(i, len(nums)):
                dfs(path + [nums[j]], n + 1, j + 1)
        
        dfs([], 0, 0)
        return res