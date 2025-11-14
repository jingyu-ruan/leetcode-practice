class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False
        
        half = total / 2
        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            nxt_dp = set()
            for j in dp:
                nxt_dp.add(j + nums[i])
                nxt_dp.add(j)
            dp = nxt_dp

        return half in dp