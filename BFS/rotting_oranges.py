class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # N is number of elements in grid
        # time complexity - O(N) since we traverse through each element once in the
        
        # nested for loop, and at most each element once through the queue
        # space complexity - O(N) since the queue will be store at most
        # the amount of elements in grid
        def inbounds(row, col, rows, cols):
            return row >= 0 and row < rows and col >= 0 and col < cols
        
        rows = len(grid)
        cols = len(grid[0])
        
        minutes = 0
        fresh = 0
        rotten_oranges = deque()
        
        for row in range(rows):
            for col in range(cols):
                orange = grid[row][col] 
                if orange == 1:
                    fresh += 1
                elif orange == 2:
                    rotten_oranges.append([row, col])
        
        while rotten_oranges:
            for i in range(len(rotten_oranges)):
                row, col = rotten_oranges.popleft()
                
                for dr, dc in [[0,1], [0,-1], [1,0], [-1,0]]:
                    r = dr + row
                    c = dc + col
                    
                    if inbounds(r, c, rows, cols) and grid[r][c] == 1:
                        # fruit has turned rotten from fresh
                        fresh -= 1
                        grid[r][c] = 2
                        rotten_oranges.append([r, c])
            minutes += 1
        if fresh != 0:
            return -1
        return max(0, minutes-1)
    
