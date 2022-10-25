class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        house_x_positions = []
        house_y_positions = []
        total_dist = 0
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    house_x_positions.append(x)
                    house_y_positions.append(y)
        
        house_x_positions.sort()
        house_y_positions.sort()
        median_x = house_x_positions[len(house_x_positions)//2]
        median_y = house_y_positions[len(house_y_positions)//2]
                
        for i in range(len(house_x_positions)):
            x = house_x_positions[i]
            y = house_y_positions[i]
            dist = abs(median_x - x) + abs(median_y - y)
            total_dist += dist
            
        return total_dist
        
