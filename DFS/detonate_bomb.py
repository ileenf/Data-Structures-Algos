class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def detonate(bombs, bomb, visited):
            visited.add(bomb)
            for adj_bomb in neighbors[bomb]:
                if adj_bomb not in visited:
                    nonlocal num_exploded
                    num_exploded += 1
                    detonate(bombs, adj_bomb, visited)

        neighbors = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                dist = ((x1-x2)**2 + (y1-y2)**2)**0.5

                if (dist <= r1):
                    # bomb2 in range of bomb1
                    neighbors[i].append(j)

                if (dist <= r2):
                    # bomb1 in range of bomb2 
                    neighbors[j].append(i)
        
        max_detonated = 0
        for bomb in range(len(bombs)):
            visited = set()
            num_exploded = 1
            detonate(bombs, bomb, visited)
            max_detonated = max(max_detonated, num_exploded)

        return max_detonated
