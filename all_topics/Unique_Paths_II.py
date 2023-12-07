class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or [1 for _ in range(n)] in obstacleGrid:
            return 0

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1
                    if i == 0:
                        for k in range(j + 1, n):
                            obstacleGrid[i][k] = -1
                    if j == 0:
                        for k in range(i + 1, m):
                            obstacleGrid[k][j] = -1
                if i == 0 and obstacleGrid[i][j] != -1:
                    obstacleGrid[i][j] = 1
                if j == 0 and obstacleGrid[i][j] != -1:
                    obstacleGrid[i][j] = 1

        # print(obstacleGrid)

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == -1:
                    continue
                if obstacleGrid[i - 1][j] == -1 and obstacleGrid[i][j - 1] == -1:
                    continue
                elif obstacleGrid[i - 1][j] == -1:
                    obstacleGrid[i][j] += obstacleGrid[i][j - 1]
                elif obstacleGrid[i][j - 1] == -1:
                    obstacleGrid[i][j] += obstacleGrid[i - 1][j]
                else:
                    obstacleGrid[i][j] += obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]

        # print(obstacleGrid)

        return 0 if obstacleGrid[m - 1][n - 1] == -1 else obstacleGrid[m - 1][n - 1]

    # 动态规划
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])

        f = [0 for _ in range(m)]

        if obstacleGrid[0][0] == 0:
            f[0] = 1

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    f[j] = 0
                    continue
                if j - 1 >= 0 and obstacleGrid[i][j - 1] == 0:
                    f[j] += f[j - 1]

        return f[len(f) - 1]