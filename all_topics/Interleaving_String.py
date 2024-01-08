class Solution:
    # 超出时间限制
    # def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    #     n, m = len(s1), len(s2)
    #     # print(n, m, len(s3))
    #     if n == m == len(s3) == 0:
    #         return True
    #     if n + m != len(s3):
    #         return False

    #     if n == 0 or m == 0:
    #         return True if s1 + s2 == s3 else False

    #     if s1 + s2 == s3 or s2 + s1 == s3:
    #         return True

    #     for i in range(len(s3)):
    #         if s3[i] == s1[0] and s3[i] == s2[0]:
    #             return self.isInterleave(s1[1:], s2[:], s3[i + 1:]) or self.isInterleave(s1[:], s2[1:], s3[i + 1:])

    #         elif s3[i] == s1[0]:
    #             return self.isInterleave(s1[1:], s2[:], s3[i + 1:])
    #         elif s3[i] == s2[0]:
    #             return self.isInterleave(s1[:], s2[1:], s3[i + 1:])
    #         else:
    #             return False

    # def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    #     n, m = len(s1), len(s2)
    #     # print(n, m, len(s3))
    #     if n == m == len(s3) == 0:
    #         return True
    #     if n + m != len(s3):
    #         return False

    #     if n == 0 or m == 0:
    #         return True if s1 + s2 == s3 else False

    #     if s1 + s2 == s3 or s2 + s1 == s3:
    #         return True

    #     dp = [[0] * (n + 1)] * (m + 1)

    #     for i in range(1, n + 1):
    #         if s3[i] == s1[i]:
    #             dp[0][i] = True

    #     for i in range(1, m + 1):
    #         if s3[i] == s2[i]:
    #             dp[i][0] = True

    #     ptr_s3 = 0
    #     for i in range(m + 1):

    #         for j in range(n + 1):
    #             if s3[ptr_s3] == s1[j]:
    #                 dp[i][j] = 1
    #             else:
    #                 continue

    # 动态规划
    # 双指针法错 -> 解决这个问题的正确方法是动态规划。
    # 定义 f(i,j) 表示 s1 的前 i 个元素和 s2 的前 j 个元素是否能交错组成 s3 的前 i+j 个元素
    # 如果 s1 的第 i 个元素和 s3 的第 i+j 个元素相等，那么 s1 的前 i 个元素和 s2 的前 j 个元素是否能交错组成 s3 的前 i+j 个元素取决于 s1 的前 i−1 个元素和 s2 的前 j 个元素是否能交错组成 s3 的前 i+j−1 个元素，即此时 f(i,j) 取决于 f(i−1,j)
    # f(i,j)=[f(i−1,j) and s1(i−1)=s3(p)]or[f(i,j−1) and s2(j−1)=s3(p)]
    # p=i+j−1。边界条件为 f(0,0)=True

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/interleaving-string/solutions/335373/jiao-cuo-zi-fu-chuan-by-leetcode-solution/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, t = len(s1), len(s2), len(s3)
        f = [[False] * (m + 1) for _ in range(n + 1)]

        if n + m != t:
            return False

        f[0][0] = True
        for i in range(n + 1):
            for j in range(m + 1):
                p = i + j - 1
                if i > 0:
                    f[i][j] = f[i][j] or (f[i - 1][j] and s1[i - 1] == s3[p])
                if j > 0:
                    f[i][j] = f[i][j] or (f[i][j - 1] and s2[j - 1] == s3[p])

        return f[n][m]

    # 滚动数组优化
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, t = len(s1), len(s2), len(s3)
        f = [False] * (m + 1)

        if n + m != t:
            return False

        f[0] = True
        for i in range(n + 1):
            for j in range(m + 1):
                p = i + j - 1
                if i > 0:
                    f[j] &= (s1[i - 1] == s3[p])
                if j > 0:
                    f[j] |= (f[j - 1] and s2[j - 1] == s3[p])

        return f[m]