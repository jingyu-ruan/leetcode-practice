class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        n = len(nums)
        cur = n - k
        last_k = []
        for i in range(cur, n):
            last_k.append(nums[i])

        for j in range(cur - 1, -1, -1):
            nums[j + k] =  nums[j]
        
        s = 0
        for l in last_k:
            nums[s] = l
            s += 1
