from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        unlock = defaultdict(list)
        need = defaultdict(int)
        for a, b in prerequisites:
            unlock[b].append(a)
            need[a] += 1
        q = deque()
        finish = 0
        for c in range(numCourses):
            if c not in need:
                q.append(c)
                # finish += 1
        while q:
            course = q.popleft()
            finish += 1
            if course in unlock:
                for i in unlock[course]:
                    need[i] -= 1
                    if need[i] == 0:
                        q.append(i)
        return True if finish == numCourses else False
        
