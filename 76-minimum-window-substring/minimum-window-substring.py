from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        
        need = Counter(t)
        fulfilled = 0
        l = 0
        window = defaultdict(int)
        min_len = float('inf')
        res = ''
        for i, v in enumerate(s):
            if v in need:
                window[v] += 1
                if window[v] == need[v]:
                    fulfilled += 1

            while fulfilled == len(need):
                d = s[l]
                if d in need:
                    window[d] -= 1
                    if window[d] < need[d]:
                        fulfilled -= 1
                l += 1
            
                if i - l + 2 < min_len:
                    min_len = i - l + 2
                    res = s[l-1:i+1]
            
        
        return res



