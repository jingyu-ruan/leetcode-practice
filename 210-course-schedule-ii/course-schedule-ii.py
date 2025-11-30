from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        unlock = defaultdict(list)
        num_needed = defaultdict(int)
        res = []
        queue = deque()

        for a, b in prerequisites:
            unlock[b].append(a)
            num_needed[a] += 1

        for c in range(numCourses):
            if num_needed[c] == 0:
                queue.append(c)
                res.append(c)
        
        while queue:
            n = len(queue)
            for _ in range(n):
                cur = queue.popleft()
                for c in unlock[cur]:
                    num_needed[c] -= 1
                    if num_needed[c] == 0:
                        queue.append(c)
                        res.append(c)

        if len(res) == numCourses:
            return res
        return []
        