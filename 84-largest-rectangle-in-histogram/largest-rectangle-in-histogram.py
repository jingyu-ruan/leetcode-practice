class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 1:
            return heights[0]
        res = 0
        stack = [0]
        heights.append(0)
        # area = 0
        for i in range(1, n + 1):
            while stack and heights[stack[-1]] > heights[i]:
                l = stack.pop()
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                res = max(res, (width) * heights[l])
            
            stack.append(i)        

        return res