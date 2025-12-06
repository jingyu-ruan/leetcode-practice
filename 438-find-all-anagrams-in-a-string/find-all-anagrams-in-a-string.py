from collections import Counter, defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = Counter(p)
        window = defaultdict(int)
        res = []
        l = 0
        fulfilled = 0

        for i, v in enumerate(s):
            if v in need:
                window[v] += 1
                if window[v] == need[v]:
                    fulfilled += 1
            
            
            if i - l + 1 > len(p):
                d = s[l]
                l += 1
                if d in need:
                    if window[d] == need[d]:
                        fulfilled -= 1 
                    window[d] -= 1
                       

            if fulfilled == len(need):
                res.append(l)
        return res            
