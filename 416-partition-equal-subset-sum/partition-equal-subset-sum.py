class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        
        need = sum(nums) / 2
        n = len(nums)
        num_set = set()
        num_set.add(0)

        for i in range(n):
            lst = list(num_set)
            for j in lst:
                num_set.add(j + nums[i])
        
        if need in num_set:
            return True
        return False