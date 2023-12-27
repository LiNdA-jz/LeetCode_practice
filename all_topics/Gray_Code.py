class Solution:
    # not work
    # def grayCode(self, n: int) -> List[int]:
    #     if n == 1:
    #         return [0, 1]

    #     res = [0]
    #     max_num = 2 ** n - 1

    #     i = n - 2
    #     cur = 0

    #     # "add" 1
    #     while i >= 0:
    #         cur += 2 ** i
    #         res.append(cur)
    #         i -= 1

    #     cur += 2 ** (n - 1)
    #     res.append(cur)
    #     # print(cur)
    #     # "change to" 0
    #     i = 0
    #     while i < n - 1:
    #         cur -= 2 ** i
    #         res.append(cur)
    #         i += 1

    #     i = 0
    #     while i < n - 2:
    #         cur += 2 ** i
    #         res.append(cur)
    #         i += 1

    #     if n % 2 == 1:
    #         res.append(1)

    #     # print(cur)
    #     return res

    # 归纳法
    # 格雷编码
    # 如果我们获取到了 n−1 位的格雷码序列，记为 Gn−1，我们可以使用它构造出 n 位的格雷码序列 Gn
        # 将 Gn−1 复制一份并翻转，记为 G_{n-1}^T
        # 给 G_{n-1}^T 中每个元素的第 n-1 个二进制位都从0 变为1，得到 （G_{n-1}^T)'。最低的二进制位为第0个二进制位
        # 将 G_{n-1}^T 和 （G_{n-1}^T)' 进行拼接，得到 Gn


    # def grayCode(self, n: int) -> List[int]:
    #     ans = [0]
    #     for i in range(1, n + 1):
    #         for j in range(len(ans) - 1, -1, -1):
    #             ans.append(ans[j] | (1 << (i - 1)))
    #     return ans

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/gray-code/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 公式法
    # g_i = i ⊕ ⌊i / 2⌋
    # ⊕ 表示按位异或运算，不同为1，相同为0
    # 当 i 为偶数时，i 和 i+1 只有最低的一个二进制位不同，而 ⌊i/2⌋ 和 ⌊(i+1)/2⌋ 相等，因此 gi 和 g_{i+1} 也只有最低的一个二进制位不同
    # 当 i 为奇数时，我们记 i 的二进制表示为 (⋯01⋯11)_2，i+1 的二进制表示为 (⋯10⋯00)_2
        # i 和 i+1 的二进制表示的若干个最高位是相同的
        # i 和 i+1 的二进制表示从高到低的第一个不同的二进制位，i 中的二进制位为 0，而 i+1 中的二进制位为 1, 在这之后，i 的所有二进制位均为 1，i+1 的所有二进制位均为 0

    def grayCode(self, n: int) -> List[int]:
        ans = [0] * (1 << n)
        for i in range(1 << n):
            ans[i] = (i >> 1) ^ i
        return ans

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/gray-code/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。