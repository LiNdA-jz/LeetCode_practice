class Solution:
    def longestPalindrome(self, s:str)->str:
    #     pal = ""
    #     for i in range(len(s)):
    #         l, r = i, i #odd lengths
    #         found = self.findpal(s, l, r)
    #         if len(pal) < len(found):
    #             pal = found
    #         l,r = i,i+1
    #         found = self.findpal(s, l, r)
    #         if len(pal) < len(found):
    #             pal = found
    #     return pal
    # def findpal(self, s1, l, r):
    #     ls = len(s1)
    #     while l>=0 and r<ls and s1[l]==s1[r]:
    #         l-=1
    #         r+=1
    #     return s1[l+1:r]

    # Time Limit Exceeded
    # l, r = 0, len(s)

    # if s == s[::-1]:
    #     return s
    # else:
    #     if (s[l] not in s[l+1:r]):
    #         return self.longestPalindrome(s[l+1:r])
    #     elif (s[r-1] not in s[l:r-1]):
    #         return self.longestPalindrome(s[l:r-1])
    #     else:
    #         l1 = self.longestPalindrome(s[l+1:r])
    #         l2 = self.longestPalindrome(s[l:r-1])
    #         return l1 if len(l1) > len(l2) else l2

        longest_palindrom = ''
        dp = [[0] * len(s) for _ in range(len(s))]
        # filling out the diagonal by 1
        for i in range(len(s)):
            dp[i][i] = True
            longest_palindrom = s[i]

        # filling the dp table
        for i in range(len(s) - 1, -1, -1):
            # j starts from the i location : to only work on the upper side of the diagonal
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:  # if the chars mathces
                    # if len slicied sub_string is just one letter if the characters are equal, we can say they are palindomr dp[i][j] =True
                    # if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
                    if j - i == 1 or dp[i + 1][j - 1] is True:
                        dp[i][j] = True
                        # we also need to keep track of the maximum palindrom sequence
                        if len(longest_palindrom) < len(s[i:j + 1]):
                            longest_palindrom = s[i:j + 1]

        return longest_palindrom