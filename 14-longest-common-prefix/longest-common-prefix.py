class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 1:
            return strs[0]
        
        i = 0
        res = ''
        while i < len(strs[0]):
            for j in range(1, n):
                s = strs[j]
                if i >= len(s):
                    return res
                if s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
            i += 1
        
        return strs[0]