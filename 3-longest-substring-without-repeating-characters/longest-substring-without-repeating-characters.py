class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        streak = 1
        left = 0
        cur_word_set = set()
        for i in range(len(s)) :
            while s[i] in cur_word_set:
                
                cur_word_set.remove(s[left])
                left += 1
            cur_word_set.add(s[i])
            max_length = max(max_length, i - left + 1)
        return max_length