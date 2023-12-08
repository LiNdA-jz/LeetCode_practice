class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        min_sum = grid[0][0]
        m, n = len(grid), len(grid[0])

        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]

        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i -1][j], grid[i][j - 1])

        return grid[m - 1][n - 1]

    # 动态规划
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, columns = len(grid), len(grid[0])
        dp = [[0] * columns for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, columns):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[rows - 1][columns - 1]

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/minimum-path-sum/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。