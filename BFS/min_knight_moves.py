class Solution:
    def minKnightMoves(self, end_x: int, end_y: int) -> int:
        end_x = abs(end_x)
        end_y = abs(end_y)
        directions = [[2, 1], [1, 2], [-2, 1], [-1, 2],[2, -1], [1, -2]]
        queue = deque([[0,0,0]])
        seen = {(0,0)}
        
        while queue:
            x, y, move = queue.popleft()
            
            if (x, y) == (end_x, end_y):
                return move
            
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                
                if (new_x, new_y) not in seen and -2 <= new_x <= end_x +2 and -2 <= new_y <= end_y + 2:
                    queue.append([new_x, new_y, move+1])
                    seen.add((new_x, new_y))
        return -1
                   
