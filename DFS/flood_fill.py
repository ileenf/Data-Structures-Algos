class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        seen = set()
        def inbounds(row, col):
            return row >= 0 and row < rows and col >= 0 and col < cols
            
        def dfs(row, col, val):
            if (row, col) in seen or not inbounds(row, col):
                return
            seen.add((row,col))
            
            if image[row][col] == val:
                image[row][col] = newColor
                    
                for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                    x = dx + row
                    y = dy + col
                
                    dfs(x, y, val)

        dfs(sr, sc, image[sr][sc])
        return image
