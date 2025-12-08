class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n
        max_left = 0
        max_right = 0
        for i in range(n):
            left[i] = max_left
            max_left = max(max_left, height[i])
        
        for i in range(n - 1, -1, -1):
            right[i] = max_right
            max_right = max(max_right, height[i])
        
        res = 0
        for i in range(n):
            res += max(0, min(left[i], right[i]) - height[i])
        
        return res