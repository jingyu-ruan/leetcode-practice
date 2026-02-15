from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        need = defaultdict(int)
        unlock = defaultdict(list)
        for a, b in prerequisites:
            unlock[b].append(a)
            need[a] += 1
        q = deque()
        finished = 0
        for i in range(numCourses):
            if i not in need:
                q.append(i)
        while q:
            course = q.popleft()
            finished += 1
            for i in unlock[course]:
                need[i] -= 1
                if need[i] == 0:
                    q.append(i)

        return True if finished == numCourses else False
        