class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def palindrome(word):
            l = 0
            r = len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True

        def bt(start, path):
            if start == len(s):
                res.append(path[:])
                return 
            
            for end in range(start, len(s)):
                sub = s[start:end + 1]
                if palindrome(sub):
                    path.append(sub)
                    bt(end + 1, path)
                    path.pop()

        bt(0, [])    
        return res    
            

