class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 1:
            return heights[0]
        left = [0] * n
        right = [0] * n
        res = 0
        stack = []
        for i, v in enumerate(heights):
            while stack and heights[stack[-1]] >= v:
                stack.pop()
            if not stack:
                left[i] = -1
            else:
                left[i] = stack[-1]
            stack.append(i)
        
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                right[i] = n
            else:
                right[i] = stack[-1]
            stack.append(i)

        for i in range(n):
            res = max(res, heights[i] * (right[i] - left[i] - 1))

        return res