class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        
        def inbounds(row, col):
            return row >= 0 and row < rows and col >= 0 and col < cols
        
        def dfs(row, col, direction):
            if not inbounds(row, col):
                return
            if (row, col) in seen or grid[row][col] == 0:
                return 
            seen.add((row, col))
            
            path.append(direction)
            dfs(row+1, col, 'D')
            dfs(row-1, col, 'U')
            dfs(row, col+1, 'R')
            dfs(row, col-1, 'L')
            # record when backtracking happens
            path.append('0')
        
        unique_islands = set()
        for row in range(rows):
            for col in range(cols):
                path = []
                dfs(row, col, '')
                if path:
                    unique_islands.add(tuple(path))
        return len(unique_islands)
