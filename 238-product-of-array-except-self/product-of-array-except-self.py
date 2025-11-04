class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [1] * n
        r = [1] * n
        res = [1] * n

        # 左积
        for i in range(1, n):
            l[i] = l[i - 1] * nums[i - 1]
        
        # 右积
        for j in range(n - 2, -1, -1):
            r[j] = r[j + 1] * nums[j + 1]

        # 合并
        for k in range(n):
            res[k] = l[k] * r[k]

        return res
        