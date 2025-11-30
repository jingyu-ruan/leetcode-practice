from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        m = len(board)
        n = len(board[0])
        flatten = []
        is_even_row = True
        for row in board[::-1]: 
            if is_even_row:
                flatten.extend(row)        # 正向 [1, 2, 3]
            else:
                flatten.extend(row[::-1])  # 反向 [6, 5, 4]
            is_even_row = not is_even_row  # 每换一行，方向变一次

        queue = deque([1])
        visited = {1}
        res = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                cur = queue.popleft()
                for i in range(1, 7):
                    if cur + i <= m * m and cur + i not in visited and flatten[cur + i - 1] == -1:
                        queue.append(cur + i)
                        visited.add(cur + i)
                    elif cur + i <= m * m and flatten[cur + i - 1] not in visited and flatten[cur + i - 1] != -1:
                        queue.append(flatten[cur + i - 1])
                        visited.add(flatten[cur + i - 1])
            
            res += 1
            if m * m in queue:
                return res

        return -1

