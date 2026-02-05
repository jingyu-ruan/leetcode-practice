from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque()
        # [3]
        for i in range(k - 1): # k - 1 = 2
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            stack.append(i)
        n = len(nums)
        res = []
        for i in range(k - 1, n): # k = 3, k - 1 = 2
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            stack.append(i)
            res.append(nums[stack[0]])
            if stack[0] + k == i + 1:
                stack.popleft()
        
        return res

