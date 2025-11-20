from collections import Counter, defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        need = Counter(p)
        cur = defaultdict(int)
        #need_len = len(need)
        #cur_len = 0
        # l = 0
        res = []
        # create window
        for i in range(len(p)):
            cur[s[i]] += 1
        
        if cur == need:
            res.append(0)
        
        for r in range(len(p), len(s)):
            cur[s[r]] += 1
            cur[s[r-len(p)]] -= 1
            if cur[s[r-len(p)]] == 0:
                del cur[s[r-len(p)]]
            if cur == need:
                res.append(r - len(p) + 1)
            
        
        return res