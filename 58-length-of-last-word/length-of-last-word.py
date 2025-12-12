class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        for ch in s[::-1]:
            if ch != ' ':
                res += 1
            if ch == ' ':
                if res != 0:
                    return res
        
        return res
