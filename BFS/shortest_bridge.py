class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def in_bounds(row, col):
            return row >= 0 and row < rows and col >= 0 and col < cols
       
        def get_first_island(row, col):
            first_island_pos.append((row, col))
            grid[row][col] = -1

            for dr, dc in [[0,1], [1,0], [-1,0], [0,-1]]:
                adj_row = dr + row
                adj_col = dc + col
                if in_bounds(adj_row, adj_col) and grid[adj_row][adj_col] == 1:
                    get_first_island(adj_row, adj_col) 

        rows = len(grid)
        cols = len(grid[0])

        first_island_pos = deque()
        distance = 0

        seen_first_island = False
        # get all row, col coords for the first island
        for row in range(rows):
            for col in range(cols):
                if not seen_first_island and grid[row][col] == 1:
                    get_first_island(row, col)
                    seen_first_island = True

        while first_island_pos:
            # for each layer, increment distance if water and return distance if reached second island
            next_water_layer = []
            for row, col in first_island_pos:
                for dr, dc in [[0,1], [1,0], [-1,0], [0,-1]]:
                    adj_row = dr + row
                    adj_col = dc + col

                    if in_bounds(adj_row, adj_col):
                        if grid[adj_row][adj_col] == 1:
                            return distance
                        elif grid[adj_row][adj_col] == 0:
                            next_water_layer.append([adj_row, adj_col])
                            grid[adj_row][adj_col] = -1

            distance += 1
            first_island_pos = next_water_layer
