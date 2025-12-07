class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        if n == 1:
            return res
        stack = []
        for i, v in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < v:
                prev_i = stack.pop()
                res[prev_i] = i - prev_i
            
            stack.append(i)
        
        return res