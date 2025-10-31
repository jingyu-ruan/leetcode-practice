class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cur = 0
        cur_word = word[cur]
        m = len(board)
        n = len(board[0])

        def dfs(r, c, cur):
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[cur]:
                return False
            if cur == len(word) - 1:
                return True
            
            temp = board[r][c]  # 保存
            board[r][c] = '#'
            
            found = (  # 先递归搜索并保存结果
                    dfs(r + 1, c, cur + 1) or
                    dfs(r - 1, c, cur + 1) or
                    dfs(r, c + 1, cur + 1) or
                    dfs(r, c - 1, cur + 1)
                )

            board[r][c] = temp  # 再恢复现场
            return found 

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False
    
