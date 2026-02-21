class Solution:
    def isPalindrome(self, s: str) -> bool:
        pure = ''
        for ch in s:
            if ch.isalpha():
                pure += ch.lower()
            if ch.isdigit():
                pure += ch
        l, r = 0, len(pure) - 1
        while l < r:
            if pure[l] != pure[r]:
                return False
            l += 1
            r -= 1
        
        return True