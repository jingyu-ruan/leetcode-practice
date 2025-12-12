class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        post = [1] * n
        prod = nums[0]
        res = [1] * n
        for i in range(1, n):
            pre[i] = prod
            prod *= nums[i]
        
        prod = nums[-1]
        for i in range(n - 2, -1, -1):
            post[i] = prod
            prod *= nums[i]
        
        for i in range(n):
            res[i] = pre[i] * post[i]
        
        return res
        