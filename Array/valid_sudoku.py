class Solution:
    # N = 9 (or for general case, = N x N board)
    # time and space: O(1) because dimensions of board is fixed,
    # therefore traverse through 81 elements and store max 81 elements.
    # time complexity (general): O(N^2), iterate through each element
    # when creating index dict, iterate through max N x N elements
    # in dict.
    # space complelxity (general): O(N^2), dict will store max N x N
    # indexes if each entry in board has a number. sets also store, but it
    # is max N elements since there are N rows, N cols, and N sub boxes.
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        indexes = defaultdict(list)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                num = board[row][col]
                if num != '.':
                    indexes[num].append([row, col])
        
        for num, locations in indexes.items():
            rows = set()
            cols = set()
            sub_box = set()
            for row, col in locations:
                if row in rows:
                    return False
                rows.add(row)
                
                if col in cols:
                    return False
                cols.add(col)
                
                if (row//3, col//3) in sub_box:
                    return False
                sub_box.add((row//3, col//3))
        return True
        
