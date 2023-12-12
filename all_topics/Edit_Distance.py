class Solution:
    # not work
    # def minDistance(self, word1: str, word2: str) -> int:
    #     m, n = len(word1), len(word2)

    #     if m < n:
    #         m, n = n, m
    #         word1, word2 = word2, word1

    #     if n == 0:
    #         return m

    #     left = 0
    #     dist = 0

    #     for i in range(m):
    #         if left > n - 1:
    #             return dist + m - 1 - i
    #         if word1[i] != word2[left]:
    #             dist += 1

    #         left += 1

    #     return dist

    # 动态规划
    # 如果我们知道 horse 到 ro 的编辑距离为 a，那么显然 horse 到 ros 的编辑距离不会超过 a + 1
    # 如果我们知道 hors 到 ros 的编辑距离为 b，那么显然 horse 到 ros 的编辑距离不会超过 b + 1
    # 如果我们知道 hors 到 ro 的编辑距离为 c，那么显然 horse 到 ros 的编辑距离不会超过 c + 1
    # 从 horse 变成 ros 的编辑距离应该为 min(a + 1, b + 1, c + 1)
    # 当我们获得 D[i][j-1]，D[i-1][j] 和 D[i-1][j-1] 的值之后就可以计算出 D[i][j]
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        # 有一个字符串为空串
        if n * m == 0:
            return n + m

        # DP 数组
        D = [[0] * (m + 1) for _ in range(n + 1)]

        # 边界状态初始化
        for i in range(n + 1):
            D[i][0] = i
        for j in range(m + 1):
            D[0][j] = j

        # 计算所有 DP 值
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = D[i - 1][j] + 1
                down = D[i][j - 1] + 1
                left_down = D[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                D[i][j] = min(left, down, left_down)

        return D[n][m]

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/edit-distance/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。