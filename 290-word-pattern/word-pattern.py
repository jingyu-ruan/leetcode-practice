class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strs = s.split()
        n = len(strs)
        n2 = len(pattern)
        if n != n2:
            return False
        maps1 = {}
        maps2 = {}
        for i in range(n):
            if pattern[i] not in maps1:
                maps1[pattern[i]] = strs[i]
            else:
                if maps1[pattern[i]] != strs[i]:
                    return False
        
        for i in range(n):
            if strs[i] not in maps2:
                maps2[strs[i]] = pattern[i]
            else:
                if maps2[strs[i]] != pattern[i]:
                    return False
        
        return True
