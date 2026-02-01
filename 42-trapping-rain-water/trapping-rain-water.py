class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n
        pre = height[0]
        for i in range(1, n):
            left[i] = pre
            pre = max(pre, height[i])
        post = height[-1]
        for i in range(n - 2, -1, -1):
            right[i] = post
            post = max(post, height[i])
        
        res = 0
        for i in range(1, n - 1):
            res += max(0, min(left[i], right[i]) - height[i])
        
        return res