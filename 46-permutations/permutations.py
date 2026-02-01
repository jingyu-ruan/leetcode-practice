class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        occur = set()
        res = []
        def dfs(n, path):
            if n == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] not in occur:
                    occur.add(nums[i])
                    dfs(n + 1, path + [nums[i]])
                    occur.remove(nums[i])
        
        dfs(0, [])
        return res