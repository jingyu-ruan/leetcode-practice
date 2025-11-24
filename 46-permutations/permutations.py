class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        
        res = []
        path = []

        def dfs(lst):
            n = len(lst)
            if len(path) == n:
                res.append(path[:])
                return
            for i in range(n):
                if lst[i] not in path:
                    path.append(lst[i])
                    dfs(lst)
                    path.pop()

        dfs(nums)

        return res