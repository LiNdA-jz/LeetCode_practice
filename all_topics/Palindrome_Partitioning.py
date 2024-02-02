class Solution:
    # not work
    # def partition(self, s: str) -> List[List[str]]:
    #     n = len(s)

    #     if n <= 1:
    #         return [list(s)]

    #     res = [list(s)]

    #     def check(sub_str):
    #         n = len(sub_str)
    #         pal_ls = []
    #         if n == 1:
    #             return [[n]]

    #         dp = [[0] * n for _ in range(n)]

    #         for i in range(n):
    #             for j in range(n):
    #                 if i == j:
    #                     dp[i][j] = 1

    #         for i in range(n - 2, -1, -1):
    #             for j in range(i + 1, n):
    #                 if (s[j] == s[i] and dp[i + 1][j - 1] == 1) or dp[i + 1][j] == 1:
    #                     dp[i][j] = 1
    #                     pal_ls.append(s[i:j])

    #         print(pal_ls)

    #     check(s)
    #     return res

    # 回溯 + 动态规划预处理
    # 使用搜索 + 回溯的方法枚举所有可能
    # 当前搜索到字符串的第 i 个字符, s[0..i−1] 位置的所有字符已经被分割成若干个回文串, 枚举下一个回文串的右边界 j, 使得 s[i..j] 是一个回文串
    # 从 i 开始，从小到大依次枚举 j, 对于当前枚举的 j 值，我们使用双指针的方法判断 s[i..j] 是否为回文串
    # 如果是, 加入答案数组 ans 中, 并以 j+1 作为新的 i 进行下一层搜索, 并在未来的回溯时将 s[i..j] 从 ans 中移除
    # 字符串 s 的每个子串 s[i..j] 是否为回文串预处理出来, 使用动态规划
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        f = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

        ret = list()
        ans = list()

        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return

            for j in range(i, n):
                if f[i][j]:
                    ans.append(s[i:j+1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        return ret

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/palindrome-partitioning/solutions/639633/fen-ge-hui-wen-chuan-by-leetcode-solutio-6jkv/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 回溯 + 记忆化搜索
    # 动态规划预处理计算出了任意的 s[i..j] 是否为回文串，我们也可以将这一步改为记忆化搜索。
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        ret = list()
        ans = list()

        @cache
        def isPalindrome(i: int, j: int) -> int:
            if i >= j:
                return 1
            return isPalindrome(i + 1, j - 1) if s[i] == s[j] else -1

        def dfs(i: int):
            if i == n:
                ret.append(ans[:])
                return

            for j in range(i, n):
                if isPalindrome(i, j) == 1:
                    ans.append(s[i:j + 1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        isPalindrome.cache_clear()
        return ret

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/palindrome-partitioning/solutions/639633/fen-ge-hui-wen-chuan-by-leetcode-solutio-6jkv/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。