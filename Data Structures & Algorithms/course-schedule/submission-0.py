from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        q = deque(v for v in range(numCourses) if indegree[v] == 0)

        order = []

        while q:
            prereq = q.popleft()
            order.append(prereq)

            for course in graph[prereq]:
                indegree[course] -= 1

                if indegree[course] == 0:
                    q.append(course)
        
        return True if len(order) == numCourses else False

        