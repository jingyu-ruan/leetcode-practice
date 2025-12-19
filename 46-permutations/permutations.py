class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(path, num_set, i):
            if i == n:
                res.append(path[:])
            
            for j in range(n):
                if nums[j] not in num_set:
                    dfs(path + [nums[j]], num_set.union({nums[j]}), i + 1)
        
        dfs([], set(), 0)

        return res