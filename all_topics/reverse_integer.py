import math


class Solution:
    def reverse(self, x: int) -> int:
        # res = 0
        # MAX = 2147483647
        # MIN = -2147483648
        # while x:
        #     digit = int(math.fmod(x, 10))
        #     x = int(x / 10)
        #     if (res > MAX//10 or (res==MAX//10 and digit>MAX%10)):
        #         return 0
        #     elif (res < MIN//10 or (res==MIN//10 and digit<MIN%10)):
        #         return 0
        #     else:
        #         res = (res * 10) + digit
        #
        # return res

        # not work for 1534236469
        # if (x>2**31 - 1) or (x<-(2**31)):
        #     return 0

        # pos = True if x > 0 else False

        # x = abs(x)
        # rev_ls = []

        # while x>= 10:
        #     num = x % 10
        #     rev_ls.append(num)

        #     x //= 10
        # rev_ls.append(x)

        # res = 0
        # num_len = len(rev_ls)
        # for i in range(num_len):
        #     res += rev_ls[i] * 10 ** (num_len - i - 1)

        # return res if pos else -res

        rev = 0
        sign = 1 if x >= 0 else -1
        x *= sign
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        rev *= sign
        return rev if rev >= -(2 ** 31) and rev <= (2 ** 31 - 1) else 0