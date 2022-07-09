class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows = len(grid2)
        cols = len(grid2[0])
        seen = set()
        sub_islands = 0
        
        def inbounds(row, col):
            return row >= 0 and row < rows and col >= 0 and col < cols
        
        def dfs(row, col):
            flag = True
            grid2[row][col] = 0
            
            if grid1[row][col] != 1:
                flag = False
            
            for dr, dc in [[0,1], [0,-1], [1,0], [-1,0]]:
                r = dr + row
                c = dc + col
                
                if inbounds(r, c) and grid2[r][c] == 1:
                    flag &= dfs(r, c)
                    
            return flag
                
        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] == 1 and grid1[row][col] == 1:
                    grid2[row][col] = 0
                    if dfs(row, col):
                        sub_islands += 1
                        
        return sub_islands
