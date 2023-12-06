class Solution:
    # 超出时间限制
    # def uniquePaths(self, m: int, n: int) -> int:
    #     if m == 1 or n == 1:
    #         return 1
    #     if n == 2:
    #         return m
    #     if m == 2:
    #         return n

    #     if m == 3:
    #         return int(n * (n + 1) / 2)
    #     if n == 3:
    #         return int(m * (m + 1) / 2)

    #     paths = 0

    #     if m > n:
    #         m, n = n, m
    #     m -= 1
    #     for i in range(1, n + 1):
    #         # print(m, i)
    #         paths += self.uniquePaths(m, i)

    #     # print(paths)
    #     return paths

    # 动态规划
    # f(i,j) 表示从左上角走到 (i,j) 的路径数量；i 和 j 的范围分别是 [0,m) 和 [0,n)
    # f(i,j)=f(i−1,j)+f(i,j−1)
    # 如果 i=0，那么 f(i−1,j) 并不是一个满足要求的状态，我们需要忽略这一项；同理，如果 j=0，那么 f(i,j−1) 并不是一个满足要求的状态，我们需要忽略这一项。
    # 初始条件为 f(0,0)=1
    # 最终的答案即为 f(m−1,n−1)
    # 将所有的 f(0,j) 以及 f(i,0) 都设置为边界条件，它们的值均为 1

    def uniquePaths(self, m: int, n: int) -> int:
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print(f)
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/unique-paths/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 由于 f(i,j) 仅与第 i 行和第 i−1 行的状态有关，因此我们可以使用滚动数组代替代码中的二维数组，使空间复杂度降低为 O(n)

    def uniquePaths(self, m: int, n: int) -> int:
        f = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                f[j] += f[j - 1]
        return f[n - 1]

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/unique-paths/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 组合数学
    # 从左上角到右下角的过程中，我们需要移动 m+n−2 次，其中有 m−1 次向下移动，n−1 次向右移动
    # C_(m+n-2)^(m-1) = (m+n-2)! / (m-1)!(n-1)!
    # 可以调用 API 计算
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, n - 1)

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/unique-paths/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。