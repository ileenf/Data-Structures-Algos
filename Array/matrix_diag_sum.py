class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0

        col_left = 0
        col_right = len(mat[0])-1

        if len(mat) % 2 == 0:
            num_rows = len(mat) // 2
        else:
            num_rows = len(mat) // 2 + 1

        for row in range(num_rows):
            if col_left == col_right:
                total += mat[row][col_left]
                continue
       
            total += mat[row][col_left]
            total += mat[row][col_right]

            total += mat[len(mat) - row - 1][col_left]
            total += mat[len(mat) - row - 1][col_right]

            col_left += 1
            col_right -= 1

        return total
