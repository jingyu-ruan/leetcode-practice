class Solution:
    def countSubstrings(self, s: str) -> int:
        # cnt = len(s)

        if len(s) < 2:
            return len(s)

        def expand(left, right) -> str:
            cnt = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                cnt += 1
            return cnt
        ans = 0
        for i in range(len(s)):
            ans += expand(i, i)
            ans += expand(i, i+1)

        return ans