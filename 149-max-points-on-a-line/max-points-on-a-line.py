class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        res = 1
        from collections import defaultdict

        for i in range(len(points)):
            p1 = points[i]
            slope_count = defaultdict(int)
            same_point = 0  # count of identical points to p1
            max_same_slope = 0

            for j in range(i + 1, len(points)):
                p2 = points[j]

                # Check if same point
                if p1[0] == p2[0] and p1[1] == p2[1]:
                    same_point += 1
                else:
                    # Compute normalized slope as (dx, dy) tuple
                    dx = p2[0] - p1[0]
                    dy = p2[1] - p1[1]

                    # Reduce by GCD to get canonical form
                    g = self.gcd(abs(dx), abs(dy))
                    dx //= g
                    dy //= g

                    # Normalize sign: ensure dx >= 0, or if dx == 0 then dy > 0
                    if dx < 0 or (dx == 0 and dy < 0):
                        dx = -dx
                        dy = -dy

                    slope = (dx, dy)
                    slope_count[slope] += 1
                    max_same_slope = max(max_same_slope, slope_count[slope])

            # Total points on line through p1: same points + most frequent slope group
            total = same_point + max_same_slope + 1  # +1 for p1 itself
            res = max(res, total)

        return res

    def gcd(self, a: int, b: int) -> int:
        return a if b == 0 else self.gcd(b, a % b)