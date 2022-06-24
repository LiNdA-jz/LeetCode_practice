class Solution:
    def myAtoi(self, s: str) -> int:
        # leading whitespace
        s = s.lstrip(" ")
        # positive / negative
        sign = 0
        if (s[0]=="+"):
            s = s[1:]
            sign = 1
        elif (s[0]=="-"):
            s = s[1:]
            sign =-1
        # convert
        for i in range(len(s)):
            if not (s[i].isdigit()):
                s = s[:i]
                break
        if (len(s)==0):
            return 0
        res = sign
        MAX = 2147483647
        MIN = -2147483648
        
        for i in range(len(s)-1):
            digit = int(s[i])
            res = res*10 + digit
        
        if ((res>MAX//10 or (res==MAX//10 and int(s[len(s)-1]>MAX%10)))):
            return MAX
        elif ((res<MIN//10 or (res==MIN//10 and int(s[len(s)-1]<MIN%10)))):
            return MIN
        else:
            digit = int(s[len(s)-1])
            res = res*10 + digit
            
        if not (sign==0):
            res *= sign
        
        return res