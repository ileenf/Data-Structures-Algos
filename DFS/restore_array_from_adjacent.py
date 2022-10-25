class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        neighbors = defaultdict(list)
        
        for num1, num2 in adjacentPairs:
            neighbors[num1].append(num2)
            neighbors[num2].append(num1)
        
        visited = set()
        original = []
        
        for num, adjacent in neighbors.items():
            if len(adjacent) == 1:
                original.append(num)
                break
        
        def traverse_adjacent_pair(num):
            visited.add(num)
            
            for adjacent_num in neighbors[num]:
                if adjacent_num not in visited:
                    original.append(adjacent_num)
                    traverse_adjacent_pair(adjacent_num)
                    
        traverse_adjacent_pair(original[0])
        return original
