class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def search_province(graph, start, visited):
            if start in visited:
                return 0

            visited.add(start)

            num_cities = 1
            for city in graph[start]:
                num_cities += search_province(graph, city, visited)
            return num_cities

        graph = {n + 1: set() for n in range(len(isConnected))}

        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if isConnected[row][col] == 1 and row != col:
                    a = row + 1
                    b = col + 1
                    graph[a].add(b)
                    graph[b].add(a)

        visited = set()
        num_provinces = 0

        for city in graph:
            num_connected = search_province(graph, city, visited)
            if num_connected > 0: 
                num_provinces += 1

        return num_provinces
