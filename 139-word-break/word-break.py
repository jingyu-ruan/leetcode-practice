class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        # T F F F F F F F F 
        # # l e e t c o d e
        s2 = '#' + s
        for i, ch in enumerate(s2):
            for j in range(i):
                if dp[j] and s2[j+1:i+1] in word_set:
                    dp[i] = True

        return dp[-1]

