class Solution:
    # not work
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     if len(triangle) == 1:
    #         return triangle[0][0]

    #     if len(triangle) == 2:
    #         return triangle[0][0] + min(triangle[1])

    #     cum_sum = triangle[-1]

    #     def backtrack(triangle, cur_sum, cur_idx):
    #         if len(triangle) == 2:
    #             return triangle[0][0] + min(triangle[1]) + cur_sum

    # 非常经典且历史悠久的动态规划题
    # 动态规划
    # 用 f[i][j] 表示从三角形顶部走到位置 (i,j) 的最小路径和
    # 想走到位置 (i,j)，上一步就只能在位置 (i−1,j−1) 或者位置 (i−1,j)
    # f[i][j]=min(f[i−1][j−1],f[i−1][j])+c[i][j]
    # f[i][0]=f[i−1][0]+c[i][0]
    # f[i][i]=f[i−1][i−1]+c[i][i]
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     n = len(triangle)
    #     f = [[0] * n for _ in range(n)]
    #     f[0][0] = triangle[0][0]

    #     for i in range(1, n):
    #         f[i][0] = f[i - 1][0] + triangle[i][0]
    #         for j in range(1, i):
    #             f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]
    #         f[i][i] = f[i - 1][i - 1] + triangle[i][i]

    #     return min(f[n - 1])

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/triangle/solutions/329143/san-jiao-xing-zui-xiao-lu-jing-he-by-leetcode-solu/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 动态规划 + 空间优化
    # f[i][j] 只与 f[i−1][..] 有关
    # 使用两个长度为 n 的一维数组进行转移，将 i 根据奇偶性映射到其中一个一维数组，那么 i−1 就映射到了另一个一维数组。这样我们使用这两个一维数组，交替地进行状态转移
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     n = len(triangle)
    #     f = [[0] * n for _ in range(2)]
    #     f[0][0] = triangle[0][0]

    #     for i in range(1, n):
    #         curr, prev = i % 2, 1 - i % 2
    #         f[curr][0] = f[prev][0] + triangle[i][0]
    #         for j in range(1, i):
    #             f[curr][j] = min(f[prev][j - 1], f[prev][j]) + triangle[i][j]
    #         f[curr][i] = f[prev][i - 1] + triangle[i][i]

    #     return min(f[(n - 1) % 2])

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/triangle/solutions/329143/san-jiao-xing-zui-xiao-lu-jing-he-by-leetcode-solu/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 只需要一个长度为 n 的一维数组 f，就可以完成状态转移
    # 只有在递减地枚举 j 时，才能省去一个一维数组
    # 算位置 (i,j) 时，f[j+1] 到 f[i] 已经是第 i 行的值
    # f[0] 到 f[j] 仍然是第 i−1 行的值
    # f[j]=min(f[j−1],f[j])+c[i][j]
    # 在 (i−1,j−1) 和 (i−1,j) 中进行选择
    # 如果我们递增地枚举 j
    # 计算位置 (i,j) 时，f[0] 到 f[j−1] 已经是第 i 行的值
    # 如果我们仍然使用上述状态转移方程，那么是在 (i,j−1) 和 (i−1,j) 中进行选择
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [0] * n
        f[0] = triangle[0][0]

        for i in range(1, n):
            f[i] = f[i - 1] + triangle[i][i]
            for j in range(i - 1, 0, -1):
                f[j] = min(f[j - 1], f[j]) + triangle[i][j]
            f[0] += triangle[i][0]

        return min(f)

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/triangle/solutions/329143/san-jiao-xing-zui-xiao-lu-jing-he-by-leetcode-solu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。