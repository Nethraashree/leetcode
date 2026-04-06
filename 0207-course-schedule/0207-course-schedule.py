from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Step 1: Build graph
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # Step 2: Queue for nodes with indegree 0
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # Step 3: Process
        count = 0

        while queue:
            course = queue.popleft()
            count += 1

            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check
        return count == numCourses