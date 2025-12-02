from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic_s = defaultdict(list)
        dic_t = defaultdict(list)
        for i, v in enumerate(s):
            dic_s[v].append(i)
        for i, v in enumerate(t):
            dic_t[v].append(i)
        val_s = set(tuple(v) for v in dic_s.values())
        val_t = set(tuple(v) for v in dic_t.values())
        for v in val_s:
            if v not in val_t:
                return False
            val_t.remove(v)

        if not val_t:
            return True
        else:
            return False
