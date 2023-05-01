class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # not work
        # word1, word2 = (word2, word1) if len(word2) > len(word1) else (word1, word2)

        # m, n = len(word1), len(word2)
        # if word2 in word1:
        #     return m - n

        # res = m - n

        # for i in range(n):
        #     if word2[i] != word1[i]:
        #         res += 1

        # return res

        n = len(word1)
        m = len(word2)

        # 有一个字符串为空串
        if n * m == 0:
            return n + m

        # DP 数组
        D = [[0] * (m + 1) for _ in range(n + 1)]

        # 边界状态初始化 -> empty string to string
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
# 复杂度分析

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/edit-distance/solution/bian-ji-ju-chi-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。