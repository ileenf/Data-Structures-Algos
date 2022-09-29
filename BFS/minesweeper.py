class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, -1), (-1, -1), (1, 1)]
        def in_bounds(row, col, rows, cols):
            return 0 <= row < rows and 0 <= col < cols

        def get_num_adjacent_bombs(board, row, col):
            bombs = 0
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                if in_bounds(new_row, new_col, len(board), len(board[0])) and board[new_row][new_col] == 'M':
                    bombs += 1
            return bombs
        
        def reveal_adjacent_squares(board, row, col):
            positions = deque()
            positions.append([row, col])
            seen = set()
            
            
            while positions:
                curr_row, curr_col = positions.popleft()
                
                bombs = get_num_adjacent_bombs(board, curr_row, curr_col)
                if bombs == 0:
                    board[curr_row][curr_col] = 'B'

                    for dr, dc in directions:
                        new_row = curr_row + dr
                        new_col = curr_col + dc
                        
                        if in_bounds(new_row, new_col, len(board), len(board[0])) and (new_row, new_col) not in seen and board[new_row][new_col] == 'E':
                            positions.append([new_row, new_col])
                            seen.add((new_row, new_col))
                else:
                    board[curr_row][curr_col] = str(bombs)
                    
        
        click_row, click_col = click
        
        if board[click_row][click_col] == 'M':
            board[click_row][click_col] = 'X'
        elif board[click_row][click_col] == 'E':
            adjacent_bombs = get_num_adjacent_bombs(board, click_row, click_col)
            
            if adjacent_bombs == 0:
                reveal_adjacent_squares(board, click_row, click_col)
            else:
                board[click_row][click_col] = str(adjacent_bombs)
        return board
