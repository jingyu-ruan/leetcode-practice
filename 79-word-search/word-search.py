class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        # cur = 0

        def bt(cur, r, c):
            if cur == len(word): 
                return True
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[cur]:
                return False
            
            tmp = board[r][c]
            board[r][c] = '#'

            found = (
                bt(cur+1, r-1, c) or
                bt(cur+1, r+1, c) or
                bt(cur+1, r, c-1) or
                bt(cur+1, r, c+1)
            )

            board[r][c] = tmp
            return found

        for i in range(m):
            for j in range(n):
                if bt(0, i, j):
                    return True
        return False

        

                        