class Solution:
    def hammingWeight(self, n: int) -> int:
        # bin_n = bin(n)[2:]

        # count_one = 0

        # for i in range(len(bin_n)):
        #     if int(bin_n[i]) == 1:
        #         count_one += 1

        # return count_one

        return bin(n)[2:].count('1')