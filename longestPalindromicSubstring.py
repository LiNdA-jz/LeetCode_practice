class Solution:
    def longestPalindrome(self, s: str) -> str:
        l, r = 0, len(s)-1
        res = []
        while (s[l] != s[r] and r>0 and l<=r):
            r -= 1
        res = s[l:r+1]

        if (len(res)==1):
            l, r = 0, len(s)-1
            res = []
            while (s[l] != s[r] and r>0 and l<=r):
                l += 1
            res = s[l:r+1]
            if (len(res)==1):
                l, r = 0, len(s)-1
                res = []
                while (s[l] != s[r] and r>0 and l<=r):
                    l += 1
                    r -= 1
                res = s[l:r+1]
        return "".join(res)