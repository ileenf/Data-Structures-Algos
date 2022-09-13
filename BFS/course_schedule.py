class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = defaultdict(int)
        graph = defaultdict(list)
        classes = 0
        for prereq in prerequisites:
            indegrees[prereq[0]] += 1
            graph[prereq[1]].append(prereq[0])
            
        queue = deque()
        for course in range(numCourses):
            if course not in indegrees:
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            classes += 1
            for neighbor in graph[course]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        return classes == numCourses
