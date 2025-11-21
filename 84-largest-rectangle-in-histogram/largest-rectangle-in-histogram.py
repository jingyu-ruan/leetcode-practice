class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stk = []
        heights.append(0)
        for i, h in enumerate(heights):
            while stk and heights[stk[-1]] > h:
                mid = stk.pop()
                height = heights[mid]
                left = stk[-1] if stk else -1
                width = i - left -1
                res = max(res, height * width)

            stk.append(i)
        return res