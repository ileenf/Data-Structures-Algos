class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        rows = len(grid)
        cols = len(grid[0])
        
        queue = deque()
        queue.append(((0, 0), 1))
        dirs = [(0,1), (1,0), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
        
        min_dist = rows*cols + 1
        while queue:
            cell, dist = queue.popleft()
            
            if cell[0] == rows-1 and cell[1] == cols-1:
                min_dist = min(min_dist, dist)
            
            for x, y in dirs:
                new_x = x + cell[0]
                new_y = y + cell[1]
                
                if new_x >= 0 and new_x < rows and new_y >= 0 and new_y < cols and grid[new_x][new_y] == 0:
                    grid[new_x][new_y] = 1
                    queue.append(((new_x, new_y), dist+1))
                    
        if min_dist == rows*cols + 1:
            return -1
        else:
            return min_dist
