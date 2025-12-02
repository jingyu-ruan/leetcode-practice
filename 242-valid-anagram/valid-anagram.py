from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = Counter(s)
        t_dic = Counter(t)
        return s_dic == t_dic