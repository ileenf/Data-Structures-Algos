class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        
        # get all cells adjecant to pacific and atlantic
        
        pacific_queue = deque()
        atlantic_queue = deque()
        
        for i in range(rows):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, cols-1))
            
        for j in range(cols):
            pacific_queue.append((0, j))
            atlantic_queue.append((rows-1, j))
            
        def bfs(queue):
            reachable = set()
            while queue:
                cell = queue.popleft()
                reachable.add(cell)
                
                for x, y in [(0,1), (1,0), (0,-1), (-1,0)]:
                    row = cell[0] + x
                    col = cell[1] + y
                    
                    if row >= 0 and row < rows and col >= 0 and col < cols and (row, col) not in reachable and heights[cell[0]][cell[1]] <= heights[row][col]:
                        
                            queue.append((row, col))
                            
            return reachable
                            
        pacific_bfs = bfs(pacific_queue)
        atlantic_bfs = bfs(atlantic_queue)
        
        return list(pacific_bfs.intersection(atlantic_bfs))
