class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        k = len(word)
        m = len(board)
        n = len(board[0])

        def dfs(r, c, i):
            if i == k:
                return True
            if r >= m or r < 0 or c >= n or c < 0:
                return False
            if board[r][c] != word[i]:
                return False

            # if board[r][c] == word[i]:
            # plus = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            letter = board[r][c]
            board[r][c] = '#'
            found = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            board[r][c] = letter

            return found
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False