class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = dict()
        def dfs(i, j, prev):
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or prev >= matrix[i][j]:
                return 0
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            left = dfs(i, j - 1, matrix[i][j])
            right = dfs(i, j + 1, matrix[i][j])
            up = dfs(i - 1, j, matrix[i][j])
            down = dfs(i + 1, j, matrix[i][j])
            
            cache[(i, j)] = max(left, right, down, up) + 1
            return cache[(i, j)]
            
        
        ans = -1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, dfs(i, j, -1))
        return ans
