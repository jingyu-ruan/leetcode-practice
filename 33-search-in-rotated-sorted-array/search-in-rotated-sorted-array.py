class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        4 5 6 7 0 1 2
        l     m     r
        '''
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
                
            if nums[l] <= nums[m]: # 左侧递增
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m + 1
            else: # 右侧递增
                if nums[m] <= target <= nums[r]:
                    l = m
                else:
                    r = m - 1
        
        return -1