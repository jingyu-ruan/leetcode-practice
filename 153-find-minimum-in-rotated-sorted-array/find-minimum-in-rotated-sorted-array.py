class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        1, 2, 3, 4, 5
        2 3 4 5 1
        3 4 5 1 2 
        l   m   r
        4 5 1 2 3
        4 5 1
        l m r
        9 1 2 3 4
        2 1
        l r
        m
        '''
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[l] < nums[r]:
                r = m - 1
            else: # nums[l] > nums[r]
                if nums[m] >= nums[l]:
                    l = m + 1
                else:
                    r = m
        return nums[l]

