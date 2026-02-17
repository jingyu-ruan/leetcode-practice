class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        jump = 1
        max_reach = nums[0]
        next_reach = nums[0]
        for i in range(n):
            if i > max_reach:
                jump += 1
                max_reach = next_reach
                if max_reach >= n - 1:
                    return jump
            next_reach = max(next_reach, i + nums[i])
        
        return jump