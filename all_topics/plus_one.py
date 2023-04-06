class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # digits[-1] += 1
        # if digits[-1] > 9:
        #     i = len(digits) - 1
        #     while i>0:
        #         if digits[i] > 9:
        #             digits[i] -= 10
        #             digits[i-1] += 1
        #         i -= 1
        #     if digits[0] > 9:
        #         digits[0] -= 10
        #         digits.insert(0, 1)
        # return digits

        # more efficient
        s = int("".join(str(i) for i in digits)) + 1
        l = []
        while s != 0:
            l.append(s % 10)
            s //= 10
        return reversed(l)