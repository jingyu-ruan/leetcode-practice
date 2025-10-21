class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_sq = 0
        while left < right:
            sq = (right - left) * min(height[left], height[right])

            if sq > max_sq:
                max_sq = sq

            if height[left] < height[right]:
                left += 1
            else :
                right -= 1
        
        return max_sq