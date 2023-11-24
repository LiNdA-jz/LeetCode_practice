class Solution:
    # not work for x = -0.99999, n = 221620
    # def myPow(self, x: float, n: int) -> float:
    #     if x == 0.0 or abs(x) == 1.0:
    #         return x if x > 0 or (x < 0 and n % 2 == 0) else -x
    #     elif n == 0:
    #         return 1.0

    #     idx = 0
    #     gt_one = 1 if x > 1.0 else -1
    #     lt_zero = 1 if x < 0.0 else 0
    #     x = abs(x)

    #     while x < 1.0:
    #         # print(x)
    #         idx += 1
    #         x *= 10
    #     print(idx)

    #     # if idx != 0 and idx * abs(n) > 10 ** 4:
    #     #     return 0.0

    #     print(x)
    #     res = 1.0
    #     if x != 1.0:
    #         for i in range(abs(n)):
    #             res *= x
    #             if res > 10 ** 4 and gt_one and n > 0:
    #                 print(res)
    #                 return 0.0
    #     print(res)

    #     # if idx != 0:
    #     res *= 10 ** (gt_one * idx * abs(n))
    #     if lt_zero and n % 2 == 1:
    #         res = -res
    #     # if not gt_one or n < 0:
    #     #     res *= 10 ** (-idx * n)
    #     # else:
    #     #     res *= 10 ** (idx * n)
    #     print(res)

    #     # print(res)
    #     # if res > 10 ** 4:
    #     #     return 0.0
    #     # else:
    #     return res if n > 0 else 1 / res
    # return x ** n

    # 快速幂 + 递归
    # 本质是分治算法
    # 从 x 开始，每次直接把上一次的结果进行平方
    # 如果 n 为偶数，那么 x^n=y^2; 如果 n 为奇数，那么 x^n=y^2 * x

    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/powx-n/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 快速幂 + 迭代
    # 递归需要使用额外的栈空间，我们试着将递归转写为迭代
    # e.g. x^77 = x * x^4 * x^8 * x^64 -> 77 的二进制表示(1001101)_2中的每个 1
    # n = 2^i_0 + 2^i_1 + ... + 2^i_k
    # x^n = x^(2^i_0) * x^(1^i_1) * ... * x^(2^i_k)
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while N > 0:
                if N % 2 == 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方
                x_contribute *= x_contribute
                # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
                N //= 2
            return ans

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/powx-n/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。