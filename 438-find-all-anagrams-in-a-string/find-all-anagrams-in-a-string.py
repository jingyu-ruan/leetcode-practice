from collections import Counter, defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = Counter(p)
        # cur = defaultdict(int)
        #need_len = len(need)
        #cur_len = 0
        #l = 0
        res = []
        for i, ch in enumerate(s):
            if i + len(p) - 1 < len(s):
                cur = Counter(s[i:i+len(p)])
                if cur == need:
                    res.append(i)
        
        return res