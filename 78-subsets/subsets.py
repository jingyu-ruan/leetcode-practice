class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        num_set = set()
        def dfs(path, idx):
            res.append(path)
            if len(path) == n:
                return

            for i in range(idx, n):
                if nums[i] not in num_set:
                    num_set.add(nums[i])
                    dfs(path + [nums[i]], i)
                    num_set.remove(nums[i])
        
        dfs([], 0)
        return res