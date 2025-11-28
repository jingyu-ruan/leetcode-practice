class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)
        true_idx = set()
        dp = [False] * n
        for i in range(n):
            if s[:i+1] in word_set:
                dp[i] = True
                true_idx.add(i)
                continue
            idx = set()
            for j in true_idx:
                if dp[j] and s[j+1:i+1] in word_set:
                    dp[i] = True
                    idx.add(i)
            true_idx.update(idx)
        
        return dp[-1]
