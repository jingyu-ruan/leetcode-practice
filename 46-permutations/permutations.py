class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        
        res = []
        num_occured = set()

        def p(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in num_occured:
                    path.append(nums[i])
                    num_occured.add(nums[i])
                    p(path)
                    num_occured.remove(nums[i])
                    path.pop()
        
        p([])

        return res
            