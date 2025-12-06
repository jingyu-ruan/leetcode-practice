class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            nums = set()
            for j in range(n):
                if board[i][j].isdigit():
                    if board[i][j] in nums:
                        return False
                    nums.add(board[i][j])
        
        for i in range(n):
            nums = set()
            for j in range(m):
                if board[j][i].isdigit():
                    if board[j][i] in nums:
                        return False
                    nums.add(board[j][i])
        
        def three(a, b):
            nums = set()
            for i in range(a, a + 3):
                for j in range(b, b + 3):
                    if board[i][j].isdigit():
                        if board[i][j] in nums:
                            return False
                        nums.add(board[i][j])
            return True
        
        check = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]

        for i, j in check:
            if not three(i, j):
                return False
        
        return True