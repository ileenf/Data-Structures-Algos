class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        seen = set()
        
        def inbounds(row, col):
            return row >= 0 and row < rows and col >= 0 and col < cols
        
        def dfs(row, col):
            if (row, col) in seen:
                return 
            seen.add((row, col))
            
            for dr, dc in [[0,1], [0,-1], [1,0], [-1,0]]:
                r = dr + row
                c = dc + col
                
                if inbounds(r, c) and grid[r][c] == '1':
                    dfs(r, c)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in seen:
                    islands += 1
                    dfs(row, col)
                    
        return islands
