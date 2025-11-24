class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        num_set = set()
        n = len(nums)
        path = []
        res = []
        def dfs():
            if len(path) == len(nums):
                res.append(path[:])
                return                
            for i in range(n):
                if nums[i] not in num_set:
                    num_set.add(nums[i])
                    path.append(nums[i])
                    dfs()
                    num_set.remove(nums[i])
                    path.pop()
        dfs()
        return res