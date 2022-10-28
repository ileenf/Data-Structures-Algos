class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def in_bounds(row, col, rows, cols):
            return row >= 0 and row < rows and col >= 0 and col < cols
            
        m = len(grid)
        n = len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        seen = set((0, 0, k))
        
        queue = deque()
        queue.append((0, 0, k, 0))
        
        while queue:
            row, col, num_obstacles, dist = queue.popleft()
            
            if row == m - 1 and col == n - 1:
                return dist
            
            for row_diff, col_diff in directions:
                new_row = row + row_diff
                new_col = col + col_diff
                
                if not in_bounds(new_row, new_col, m, n):
                    continue
                    
                new_obstacles = num_obstacles - grid[new_row][new_col]
                
                if new_obstacles >= 0 and (new_row, new_col, new_obstacles) not in seen:
                    seen.add((new_row, new_col, new_obstacles))
                    queue.append((new_row, new_col, new_obstacles, dist+1))
                
        return -1
