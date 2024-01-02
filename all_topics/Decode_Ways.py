class Solution:
    # 超出时间限制
    # def numDecodings(self, s: str) -> int:
    #     n = len(s)

    #     if n == 1:
    #         return 0 if int(s) == 0 else 1

    #     if int(s[0]) == 0:
    #         return 0

    #     if n == 2:
    #         if 0 < int(s[0]) < 3:
    #             if 0 < int(s[1]) < 7:
    #                 return 2
    #             else:
    #                 return 1
    #         elif int(s[1]) == 0:
    #             return 0
    #         else:
    #             return 1

    #     ways = 0

    #     # 1 digit
    #     ways += self.numDecodings(s[1:])

    #     # 2 digit
    #     if 0 < int(s[0]) < 3:
    #         ways += self.numDecodings(s[2:])


    #     return ways

    # 动态规划
    # 设 fi 表示字符串 s 的前 i 个字符 s[1..i] 的解码方法数
    # 在进行状态转移时，我们可以考虑最后一次解码使用了 s 中的哪些字符
        # 使用了一个字符，只要 s[i]≠0 -> fi =f_{i−1}, 其中 s[i]=0
        # 使用了两个字符, s[i−1] 不能等于 0，并且 s[i−1] 和 s[i] 组成的整数必须小于等于 26 -> fi =f_{i−2}, 其中 s[i−1]=0 并且 10⋅s[i−1]+s[i]≤26, 只有当 i>1 时才能进行转移
    # 动态规划的边界条件为：f0=1
    def numDecodings(self, s: str) -> int:
        n = len(s)
        f = [1] + [0] * n
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                f[i] += f[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i-2:i]) <= 26:
                f[i] += f[i - 2]
        return f[n]

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/decode-ways/solutions/734344/jie-ma-fang-fa-by-leetcode-solution-p8np/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # fi 的值仅与 f_{i-1} 和 f_{i-2} 有关
    # 可以使用三个变量进行状态转移，省去数组的空间
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # a = f[i-2], b = f[i-1], c = f[i]
        a, b, c = 0, 1, 0
        for i in range(1, n + 1):
            c = 0
            if s[i - 1] != '0':
                c += b
            if i > 1 and s[i - 2] != '0' and int(s[i-2:i]) <= 26:
                c += a
            a, b = b, c
        return c

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/decode-ways/solutions/734344/jie-ma-fang-fa-by-leetcode-solution-p8np/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。