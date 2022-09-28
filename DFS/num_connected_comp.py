class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        node_to_neighbors = defaultdict(list)
        
        for n1, n2 in edges:
            node_to_neighbors[n1].append(n2)
            node_to_neighbors[n2].append(n1)
        
        connected = 0
        seen = set()
        
        def mark_neighbors(node):
            seen.add(node)
            
            for neighbor in node_to_neighbors[node]:
                if neighbor not in seen:
                    mark_neighbors(neighbor)
        
        for node in range(n):
            if node not in seen:
                mark_neighbors(node)
                connected += 1
        return connected
