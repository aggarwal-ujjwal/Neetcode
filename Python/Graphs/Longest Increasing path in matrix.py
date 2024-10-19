class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ans = 0
        if not matrix:
            return ans

        m, n = len(matrix), len(matrix[0])
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        dp = [[-1 for col in range(n)] for row in range(m)]

        for i in range(m):
            for j in range(n):
                ans = max(ans, self.dfs(matrix, i, j, m, n, dp))

        return ans

    def dfs(self, matrix, i, j, m, n, dp) -> int:
        ans = 1
        if dp[i][j] != -1:
            return dp[i][j]

        for dir in self.directions:
            x, y = i + dir[0], j + dir[1]
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                ans = max(ans, self.dfs(matrix, x, y, m, n, dp) + 1)
        dp[i][j] = ans
        return ans



# both dfs and dp combniation, write dfs base condition on your own to get better clartiy