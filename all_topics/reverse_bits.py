class Solution:
    def reverseBits(self, n: int) -> int:
        # not work
        # bin_n = bin(n)
        # print(n, bin_n)
        # rev_num, i = 0, 0

        # while(bin_n != 0):
        #     a = bin_n % 10
        #     rev_num +=  a * pow(2, (32-i))
        #     bin_n //= 10
        #     i += 1

        # return rev_num

        # output = 0
        # for i in range(32):
        #     bits =n & 1
        #     output = output | bits << (31-i)
        #     n = n >> 1
        # return output

        # # Initialize the reversed number to 0
        # reversed_num = 0

        # # Iterate over all 32 bits of the given number
        # for i in range(32):
        #     # Left shift the reversed number by 1 and add the last bit of the given number to it
        #     reversed_num = (reversed_num << 1) | (n & 1)
        #     # To add the last bit of the given number to the reversed number, perform an AND operation with the given number and 1
        #     n >>= 1

        # # Return the reversed number
        # return reversed_num

        bin_convert = bin(n)
        bin_convert_2 = bin_convert[2:]
        bin_fill_zero = bin_convert_2.zfill(32)
        reverse_bin = bin_fill_zero[::-1]
        answer = int(reverse_bin, 2)
        return answer