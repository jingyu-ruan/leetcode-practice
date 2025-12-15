class WordDictionary:
    def __init__(self):
        self.dic = dict()

    def addWord(self, word: str) -> None:
        cur = self.dic
        for i in word:
            if i not in cur:
                cur[i] = dict()
            cur = cur[i]
        cur['#'] = True

    def search(self, word: str) -> bool:
        def dfs(cur, i):
            if i == len(word):
                return '#' in cur
            
            if word[i] != '.':
                if word[i] not in cur:
                    return False
                return dfs(cur[word[i]], i + 1)
            
            for nxt in cur:
                if nxt != '#':
                    if dfs(cur[nxt], i + 1):
                        return True
            
            return False
        
        return dfs(self.dic, 0)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)