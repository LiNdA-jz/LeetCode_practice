class Solution:
    def longestPalindrome(self, s:str)->str:
        pal = ""
        for i in range(len(s)):
            l, r = i, i #odd lengths
            found = self.findpal(s, l, r)
            if len(pal) < len(found):
                pal = found
            l,r = i,i+1
            found = self.findpal(s, l, r)
            if len(pal) < len(found):
                pal = found
        return pal
    def findpal(self, s1, l, r):
        ls = len(s1)
        while l>=0 and r<ls and s1[l]==s1[r]:
            l-=1
            r+=1
        return s1[l+1:r]