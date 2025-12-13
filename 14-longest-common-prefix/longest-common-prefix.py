class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 1:
            return strs[0]
        
        first = list(strs[0])
        
        for i in range(1, n):
            r = 0
            for j, ch in enumerate(strs[i]):
                if j < len(first) and ch == first[j]:
                    r += 1
                else: break
            first = first[:r]
        
        return ''.join(first)
