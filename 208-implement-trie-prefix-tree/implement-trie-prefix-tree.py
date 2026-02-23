class Trie:

    def __init__(self):
        self.trie = dict()

    def insert(self, word: str) -> None:
        cur = self.trie
        for ch in word:
            if ch not in cur:
                cur[ch] = dict()
            cur = cur[ch]
        cur['#'] = True

    def search(self, word: str) -> bool:
        cur = self.trie
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
        if '#' in cur and cur['#']:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for ch in prefix:
            if ch not in cur:
                return False
            cur = cur[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)