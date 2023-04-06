class Solution:
    def mySqrt(self, x: int) -> int:
        # # time limit exceeded
        # if (x == 0) or (x == 1):
        #     return x
        # i = 1
        # while (i*i)<x:
        #     i += 1
        # return i if i*i == x else i-1

        # pointer!!!
        if x < 2:
            return x;
        low, high = 1, x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
            else:
                high = mid - 1
        return high