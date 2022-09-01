class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.food = deque(food)
        self.height = height
        self.width = width
        self.snake = deque([[0,0]])
        self.directions = {'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]}
    
    def not_in_bounds(self, new_head):
        return new_head[0] < 0 or new_head[0] >= self.height or new_head[1] < 0 or new_head[1] >= self.width

    def get_new_head(self, direction):
        move_row = self.directions[direction][0]
        move_col = self.directions[direction][1]
        return [self.snake[-1][0] + move_row, self.snake[-1][1] + move_col]
        
    def move(self, direction: str) -> int:
        new_head = self.get_new_head(direction)
        if self.not_in_bounds(new_head) or (new_head in self.snake and new_head != self.snake[0]):
            return -1
        
        if self.food and new_head == self.food[0]:
            self.food.popleft()
        else:
            self.snake.popleft()
        self.snake.append(new_head)
        
        return len(self.snake)-1
