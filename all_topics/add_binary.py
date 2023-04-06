class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # a_int = int(a)
        # b_int = int(b)

        # sum_int = a_int + b_int

        # sum_ls = [sum_int] if sum_int<1 else []

        # while sum_int>=1:
        #     sum_ls.append(sum_int%10)
        #     sum_int //= 10
        # sum_ls = sum_ls[::-1]

        # print(sum_ls)

        # i = len(sum_ls) - 1
        # while i>0:
        #     if sum_ls[i]>1:
        #         sum_ls[i-1] += sum_ls[i] // 2
        #         sum_ls[i] = sum_ls[i] % 2
        #     i -= 1

        # if sum_ls[0]>1:
        #     res = [sum_ls[0] // 2]
        #     sum_ls[0] = sum_ls[0] % 2
        #     res.extend(sum_ls)
        #     # print(res)
        #     return "".join(str(i) for i in res)
        # else:
        #     # print(sum_ls)
        #     return "".join(str(i) for i in sum_ls)

        # List to store the result
        result = []
        # Variable to store the carry-over value
        carry = 0

        # Initialize two pointers to traverse the binary strings from right to left
        i, j = len(a) - 1, len(b) - 1

        # Loop until both pointers have reached the beginning of their respective strings and there is no carry-over value left
        while i >= 0 or j >= 0 or carry:
            total = carry

            # Add the current binary digit in string a, if the pointer is still within bounds
            if i >= 0:
                total += int(a[i])
                i -= 1

            # Add the current binary digit in string b, if the pointer is still within bounds
            if j >= 0:
                total += int(b[j])
                j -= 1

            # Calculate the next binary digit in the result by taking the remainder of the sum divided by 2
            result.append(str(total % 2))

            # Calculate the next carry-over value by dividing the sum by 2
            carry = total // 2

        # Reverse the result and join the elements to form a single string
        return ''.join(reversed(result))