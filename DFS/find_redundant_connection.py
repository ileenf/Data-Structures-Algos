class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        redundant = []
        
        def creates_cycle(graph, v1, v2):
            if v1 not in seen:
                seen.add(v1)
                
                if v1 == v2:
                    return True
                
                for neighbor in graph[v1]:
                    if creates_cycle(graph, neighbor, v2):
                        return True
            return False
        
        for v1, v2 in edges:
            seen = set()
            if v1 in graph and v2 in graph and creates_cycle(graph, v1, v2):
                redundant = [v1, v2]
            graph[v1].add(v2)  
            graph[v2].add(v1)  
            
        return redundant
