class Solution:
    # 超出时间限制
    def divide(self, dividend: int, divisor: int) -> int:
        quotient = 0
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        else:
            sign = -1

        dividend, divisor = abs(dividend), abs(divisor)

        if dividend >= 2**31 - 1 and divisor <= 1 and sign == 1:
            return 2**31 - 1
        elif dividend >= 2**31 and divisor <= 1 and sign == -1:
            return -2**31

        if sign == 1:
            while dividend >= divisor and quotient < 2**31 - 1:
                dividend -= divisor
                quotient += 1
        else:
            while dividend >= divisor and quotient < 2**31:
                dividend -= divisor
                quotient += 1

        quotient *= sign

        print(quotient)

        if dividend > divisor:
            if sign == 1:
                return 2**31 - 1
            else:
                return -2**31
        else:
            return quotient

    # 二分查找
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # 考虑被除数为最小值的情况
        if dividend == INT_MIN:
            if divisor == 1:
                return INT_MIN
            if divisor == -1:
                return INT_MAX

        # 考虑除数为最小值的情况
        # abs(dividend) < abs(divisor)
        if divisor == INT_MIN:
            return 1 if dividend == INT_MIN else 0
        # 考虑被除数为 0 的情况
        if dividend == 0:
            return 0

        # 一般情况，使用二分查找
        # 将所有的正数取相反数，这样就只需要考虑一种情况
        rev = False
        if dividend > 0:
            dividend = -dividend
            rev = not rev
        if divisor > 0:
            divisor = -divisor
            rev = not rev

        # 快速乘
        def quickAdd(y: int, z: int, x: int) -> bool:
            # x 和 y 是负数，z 是正数
            # 需要判断 z * y >= x 是否成立
            result, add = 0, y
            while z > 0:
                if (z & 1) == 1:
                    # 需要保证 result + add >= x
                    if result < x - add:
                        return False
                    result += add
                if z != 1:
                    # 需要保证 add + add >= x
                    if add < x - add:
                        return False
                    add += add
                # 不能使用除法
                z >>= 1
            return True

        left, right, ans = 1, INT_MAX, 0
        while left <= right:
            # 注意溢出，并且不能使用除法
            mid = left + ((right - left) >> 1)
            check = quickAdd(divisor, mid, dividend)
            if check:
                ans = mid
                # 注意溢出
                if mid == INT_MAX:
                    break
                left = mid + 1
            else:
                right = mid - 1

        return -ans if rev else ans

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/divide-two-integers/description/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 类二分查找
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        # 考虑被除数为最小值的情况
        if dividend == INT_MIN:
            if divisor == 1:
                return INT_MIN
            if divisor == -1:
                return INT_MAX

        # 考虑除数为最小值的情况
        if divisor == INT_MIN:
            return 1 if dividend == INT_MIN else 0
        # 考虑被除数为 0 的情况
        if dividend == 0:
            return 0

        # 一般情况，使用类二分查找
        # 将所有的正数取相反数，这样就只需要考虑一种情况
        rev = False
        if dividend > 0:
            dividend = -dividend
            rev = not rev
        if divisor > 0:
            divisor = -divisor
            rev = not rev

        candidates = [divisor]
        # 注意溢出
        while candidates[-1] >= dividend - candidates[-1]:
            candidates.append(candidates[-1] + candidates[-1])

        ans = 0
        for i in range(len(candidates) - 1, -1, -1):
            if candidates[i] >= dividend:
                ans += (1 << i)
                dividend -= candidates[i]

        return -ans if rev else ans

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/divide-two-integers/description/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 每个能满足除出来的最大的2的幂都加入答案 也可以理解为每次计算出答案的32位中的某一位
    # x * 2**i = x << i
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        a, b, res = abs(dividend), abs(divisor), 0
        for i in range(31, -1, -1):
            # 2^i * b <= a 换句话说 a/b = 2^i + (a-2^i*b)/b
            if (b << i) <= a:
                res += 1 << i
                a -= b << i
        return res if (dividend > 0) == (divisor > 0) else -res

    # 作者：Benhao
    # 链接：https://leetcode.cn/problems/divide-two-integers/description/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。