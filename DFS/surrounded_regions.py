class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        seen = set()
        
        def dfs(row, col):
            if (row, col) in seen:
                return
            seen.add((row,col))
            for dir in [(1,0),(-1,0),(0,1),(0,-1)]:
                x = row + dir[0]
                y = col + dir[1]
                
                if x >= 0 and x < rows and y >=0 and y < cols and board[x][y] == "O" and (x,y) not in seen:
                    board[x][y] = 0
                    dfs(x,y)
            
        
        for row in (0, rows-1):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = 0
                    dfs(row, col)
        
        for col in (0, cols-1):
            for row in range(rows):
                if board[row][col] == "O":
                    board[row][col] = 0
                    dfs(row, col)
                    
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == 0:
                    board[row][col] = "O"
