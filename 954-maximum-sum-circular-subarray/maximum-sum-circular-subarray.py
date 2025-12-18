class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        max_sum = nums[0]
        curr_max = 0

        curr_min = 0
        min_sum = nums[0]

        for x in nums:
            # 1. 计算标准最大子数组和 (Kadane)
            curr_max = max(x, curr_max + x)
            max_sum = max(max_sum, curr_max)
            
            # 2. 计算最小子数组和 (为了处理环形情况)
            curr_min = min(x, curr_min + x)
            min_sum = min(min_sum, curr_min)
            
            # 3. 累加总和
            total += x
            
        # 特殊情况：如果所有数都是负数，max_sum 会小于 0
        # 此时 total == min_sum，会导致 (total - min_sum) = 0，这是不对的（子数组不能为空）
        # 所以这种情况下，直接返回 max_sum 即可
        if max_sum < 0:
            return max_sum
            
        # 比较：不跨越边界的最大值 vs 跨越边界的最大值
        return max(max_sum, total - min_sum)
