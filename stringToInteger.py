class Solution:
    def myAtoi(self, s: str) -> int:
        # leading whitespace
        s = s.lstrip(" ")
        if (len(s)==0):
            return 0
        # positive / negative
        sign = 1
        if (s[0]=="+"):
            s = s[1:]
            sign = 1
        elif (s[0]=="-"):
            s = s[1:]
            sign =-1
        if (len(s)==0):
            return 0
        # convert
        for i in range(len(s)):
            if not (s[i].isdigit()):
                s = s[:i]
                break
        if (len(s)==0):
            return 0
        res = 0
        MAX = 2147483647
        MIN = -2147483648
        
        for i in range(len(s)-1):
            digit = int(s[i])
            res = res*10 + digit
        
        if (res>MAX//10 or (res==MAX//10 and int(s[len(s)-1])>7)) and sign==1:
            return MAX
        elif (res>MAX//10 or (res==MAX//10 and int(s[len(s)-1])>8)) and sign==-1:
            return MIN
        else:
            digit = int(s[len(s)-1])
            res = (res*10 + digit) * sign
        
        return res