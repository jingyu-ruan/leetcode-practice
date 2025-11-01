class WordDictionary:
    class Node:
        __slots__ = ("children", "is_end")
        def __init__(self):
            self.children = {}      # key: 字母, value: Node
            self.is_end = False     # 该节点是否是某个单词的结尾

    def __init__(self):
        self.root = WordDictionary.Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = WordDictionary.Node()
            cur = cur.children[ch]
        cur.is_end = True

    def search(self, word: str) -> bool:
        # 在以 node 为根的子树里，从索引 i 开始匹配 word[i:]
        def dfs(i: int, node: WordDictionary.Node) -> bool:
            if i == len(word):
                return node.is_end

            ch = word[i]
            if ch == ".":
                # 通配符: 尝试所有子节点
                for nxt in node.children.values():
                    if dfs(i + 1, nxt):
                        return True
                return False
            else:
                # 普通字母: 必须沿着固定分支走
                if ch not in node.children:
                    return False
                return dfs(i + 1, node.children[ch])

        return dfs(0, self.root)
