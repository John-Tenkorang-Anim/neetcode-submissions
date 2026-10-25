from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        indegree = [0] * numCourses


        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        
        q = deque(course for course in range(numCourses) if indegree[course] == 0)

        order = []
        while q:
            prereq = q.popleft()
            order.append(prereq)

            for course in graph[prereq]:
                indegree[course] -= 1

                if indegree[course] == 0:
                    q.append(course)

        return order if len(order) == numCourses else []


        