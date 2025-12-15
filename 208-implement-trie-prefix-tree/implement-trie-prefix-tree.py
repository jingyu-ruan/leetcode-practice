class Trie:
    def __init__(self):
        self.dic = dict()
        self.cur = self.dic

    def insert(self, word: str) -> None:
        self.cur = self.dic
        for i in word:
            if i not in self.cur:
                self.cur[i] = dict()
            self.cur = self.cur[i]
        self.cur['#'] = True

    def search(self, word: str) -> bool:
        self.cur = self.dic
        for i in word:
            if i not in self.cur:
                return False
            self.cur = self.cur[i]
        if '#' in self.cur:
            return True
        
        return False

    def startsWith(self, prefix: str) -> bool:
        self.cur = self.dic
        for i in prefix:
            if i not in self.cur:
                return False
            self.cur = self.cur[i]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)