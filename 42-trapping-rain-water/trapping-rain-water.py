class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n

        left_max = height[0]
        for i in range(1, n):
            left[i] = left_max
            left_max = max(left_max, height[i])
        right_max = height[-1]
        for i in range(n - 2, -1, -1):
            right[i] = right_max
            right_max = max(right_max, height[i])
        
        res = 0
        for i in range(n):
            res += max(0, min(left[i], right[i]) - height[i])
        
        return res