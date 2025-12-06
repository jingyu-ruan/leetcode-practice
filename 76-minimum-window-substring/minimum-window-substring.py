from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1, n2 = len(s), len(t)
        if n2 > n1:
            return ''
        t_cnt = Counter(t)
        fulfilled = 0
        need = len(t_cnt)
        l = 0
        start = 0
        min_len = float('inf')
        window = defaultdict(int)
        for i, v in enumerate(s):
            if v in t_cnt:
                window[v] += 1
                if window[v] == t_cnt[v]:
                    fulfilled += 1
            
            while fulfilled == need:
                if i - l + 1 < min_len:
                    start = l
                    min_len = i - l + 1
                
                d = s[l]
                l += 1

                if d in t_cnt:
                    if window[d] == t_cnt[d]:
                        fulfilled -= 1
                    window[d] -= 1
        
        return "" if min_len == float('inf') else s[start : start + min_len]

