class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if not stk:
                stk.append(i)
            else:
                while stk and temperatures[stk[-1]] < t:
                    idx = stk.pop()
                    res[idx] = i - idx
                stk.append(i)
            
        return res
