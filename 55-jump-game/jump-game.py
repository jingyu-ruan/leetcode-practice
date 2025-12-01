class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        # cur_end = 0
        n = len(nums)
        for i in range(n):
            if i > far:
                return False
            far = max(far, i + nums[i])
            
        
        return True