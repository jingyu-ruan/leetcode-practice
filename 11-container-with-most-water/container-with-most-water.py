class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            lh, rh = height[l], height[r]
            minh = min(lh, rh)
            res = max(res, minh * (r - l))
            if lh <= rh:
                l += 1
            else:
                r -= 1

        return res