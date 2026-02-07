class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        def dfs(path, x, i):
            res.append(path[:])
            if x == n:
                return
            for j in range(i, n):
                if j > i and nums[j] == nums[j-1]:
                    continue
                dfs(path + [nums[j]], x + 1, j + 1)
        
        dfs([], 0, 0)
        return res