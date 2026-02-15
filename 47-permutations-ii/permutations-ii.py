class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        num_set = set()
        res = []
        nums.sort()
        def dfs(path):
            nonlocal res
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if i >= 1 and nums[i] == nums[i-1] and i - 1 not in num_set:
                    continue
                if i not in num_set:
                    num_set.add(i)
                    dfs(path + [nums[i]])
                    num_set.remove(i)
        
        dfs([])
        return res