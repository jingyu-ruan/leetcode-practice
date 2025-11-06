from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = defaultdict(int)

        for ch in s:
            dic[ch] += 1
        
        for i in t:
            if dic[i] == 0:
                return False
            
            dic[i] -= 1

        for j in dic:
            if dic[j] != 0:
                return False

        return True