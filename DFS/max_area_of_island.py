class Solution:
    # R = rows
    # C = cols
    # time complexity: O(RC), go through each cell in board
    # space complexity: O(1), no extra space for seen set. use original board
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0
            if grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col+1) + dfs(row, col-1)
                    
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))
        
        return max_area
            
