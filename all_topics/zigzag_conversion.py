class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # if (numRows==1):
        #     return s
        #
        # res = ""
        # for r in range(numRows):
        #     increment = 2 * (numRows - 1)
        #     for i in range(r, len(s), increment):
        #         res += s[i]
        #         if (r>0 and r<numRows-1 and i+increment-2*r<len(s)):
        #             res += s[i+increment-2*r]
        #
        # return res

        # not work
        # integer division or modulo by zero
        # s_len = len(s)
        # sep = numRows + numRows - 2
        # res = []

        # for j in range(numRows):
        #     res.append([])
        #     for i in range(s_len):
        #         if (j==0) or (j==numRows-1):
        #             if (i%sep == j):
        #                 res[j].append(s[i])
        #         else:
        #             if (i<numRows-1) and (i>0):
        #                 res[j].append(s[i])
        #             elif (i%sep == j):
        #                 if i<=2:
        #                     res[j].append(s[i])
        #                 else:
        #                     res[j].append(s[i-2])
        #                     res[j].append(s[i])
        #     res[j] = "".join(res[j])

        # final_res = "".join(res)
        # print(final_res)
        # return final_res

        if numRows == 1:
            return s
        answer = ''
        n = len(s)
        diff = 2 * (numRows - 1)
        diagonal_diff = diff
        second_index = 0
        index = 0
        for i in range(numRows):
            index = i
            while index < n:
                answer += s[index]
                if i != 0 and i != numRows - 1:
                    diagonal_diff = diff - 2 * i
                    second_index = index + diagonal_diff
                    if second_index < n:
                        answer += s[second_index]
                index += diff
        return answer