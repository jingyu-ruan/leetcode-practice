from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue = deque()
        unlock = defaultdict(list)
        num_needed = defaultdict(int)

        for a, b in prerequisites:
            unlock[b].append(a)
            num_needed[a] += 1
        
        for i in range(numCourses):
            if num_needed[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            for c in unlock[course]:
                num_needed[c] -= 1
                if num_needed[c] == 0:
                    queue.append(c)

        for i, v in num_needed.items():
            if v != 0:
                return False
        
        return True

