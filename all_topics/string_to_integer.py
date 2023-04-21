class Solution:
    def myAtoi(self, s: str) -> int:
        # # leading whitespace
        # s = s.lstrip(" ")
        # if (len(s)==0):
        #     return 0
        # # positive / negative
        # sign = 1
        # if (s[0]=="+"):
        #     s = s[1:]
        #     sign = 1
        # elif (s[0]=="-"):
        #     s = s[1:]
        #     sign =-1
        # if (len(s)==0):
        #     return 0
        # # convert
        # for i in range(len(s)):
        #     if not (s[i].isdigit()):
        #         s = s[:i]
        #         break
        # if (len(s)==0):
        #     return 0
        # res = 0
        # MAX = 2147483647
        # MIN = -2147483648
        #
        # for i in range(len(s)-1):
        #     digit = int(s[i])
        #     res = res*10 + digit
        #
        # if (res>MAX//10 or (res==MAX//10 and int(s[len(s)-1])>7)) and sign==1:
        #     return MAX
        # elif (res>MAX//10 or (res==MAX//10 and int(s[len(s)-1])>8)) and sign==-1:
        #     return MIN
        # else:
        #     digit = int(s[len(s)-1])
        #     res = (res*10 + digit) * sign
        #
        # return res

        # not work for "00000-42a1234"
        # if len(s) == 0:
        #     return 0
        # if len(s) == 1:
        #     if s.isdigit():
        #         return int(s)
        #     else:
        #         return 0
        # res_ls = []
        # pos = True

        # s = s.strip()
        # print(s)
        # if not re.match("^[-|+]?[0-9]+", s):
        #     return 0

        # s = s.lstrip("0")
        # for i in range(len(s)):
        #     if s[i] == "-":
        #         pos = False
        #     elif s[i] == "+":
        #         pos = True
        #     elif re.match("[0-9]", s[i]):
        #         res_ls.append(s[i])
        #     else:
        #         if res_ls:
        #             break

        # res = 0
        # num_len = len(res_ls)
        # for i in range(len(res_ls)):
        #     res += (ord(res_ls[i]) - ord("0")) * 10 ** (num_len - i - 1)

        # res = res if pos else -res

        # if res > 2**31 -1:
        #     return 2**31 - 1
        # elif res < -2**31:
        #     return -2**31
        # else:
        #     return res

        # s=s.lstrip()
        # sign,res,i=1,0,0
        # if i < len(s) and (s[i] == '-' or s[i] == '+'):
        #     if s[i] == '-':
        #         sign = -1
        #     i += 1
        # while i < len(s) and s[i].isdigit():
        #     res = res * 10 + int(s[i])
        #     i += 1
        # res = max(min(res * sign, 2**31 - 1), -2**31)
        # return res

        s = s.strip()
        if not s:
            return 0
        sign = -1 if s[0] == '-' else 1
        s = s[1:] if s[0] in ['-', '+'] else s
        res = 0
        for char in s:
            if not char.isdigit():
                break
            res = res * 10 + int(char)
            if res * sign >= 2 ** 31 - 1:
                return 2 ** 31 - 1
            if res * sign <= -2 ** 31:
                return -2 ** 31
        return res * sign