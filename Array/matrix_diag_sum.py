class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0

        for i in range(len(mat)):
            total += mat[i][i]
            total += mat[i][len(mat)-i-1]

        if len(mat) % 2 == 1:
            total -= mat[len(mat) // 2][len(mat[0]) // 2]
        return total


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
