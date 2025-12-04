class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        left = 0
        while left < n and directions[left] == 'L':
            left += 1

        right = n - 1
        while right >= 0 and directions[right] == 'R':
            right -= 1

        # 中间部分 [left, right] 里, 所有 'L' 和 'R' 都会碰撞
        res = 0
        for i in range(left, right + 1):
            if directions[i] != 'S':
                res += 1
        return res
