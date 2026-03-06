class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        num_set = set()
        n = len(nums)
        res = []
        def dfs(path):
            nonlocal res, num_set
            if len(path) == len(nums):
                res.append(path[:])
                return 
            for j in range(n):
                if j not in num_set:
                    num_set.add(j)
                    dfs(path + [nums[j]])
                    num_set.remove(j)
        
        dfs([])
        return res