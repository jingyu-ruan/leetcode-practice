class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        nums = [1,2,1,3,5,6,4]
                l     m     r
        [1,2,3,1]
         l m   r
        '''
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[m+1]:
                l = m + 1
            else:
                r = m
        
        return l