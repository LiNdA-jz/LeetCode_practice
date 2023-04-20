class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # not work
        # if (len(s) == 0):
        #     return 0

        # l, r = 0, 1
        # s_len = 1

        # while (l<len(s) and r<len(s)):
        #     if s[r] in s[l:r]:
        #         print(s[r])
        #         s_len = max(s_len, (r-l-1))
        #         l = r
        #         r += 1
        #     else:
        #         r += 1
        #         s_len += 1

        # return s_len

        # char_set = set()
        # max_len, start = 0, 0
        # for i, c in enumerate(s):
        #     while c in char_set:
        #         char_set.remove(s[start])
        #         start += 1
        #     char_set.add(c)
        #     max_len = max(max_len, i - start + 1)
        # return max_len

        # indext    0    1    2    3   4   5   6   7
        # string    a    c    b    d   b   a   c   d
        #         ^                  ^
        #         |                  |
        #         left               right
        #         seen = {a : 0, c : 1, b : 2, d: 3}
        #         # case 1: seen[b] = 2, current window  is s[0:4] ,
        #         #        b is inside current window, seen[b] = 2 > left = 0. Move left pointer to seen[b] + 1 = 3
        #         seen = {a : 0, c : 1, b : 4, d: 3}
        # indext    0    1    2    3   4   5   6   7
        # string    a    c    b    d   b   a   c   d
        #                         ^   ^
        #                         |   |
        #                     left  right
        # indext    0    1    2    3   4   5   6   7
        # string    a    c    b    d   b   a   c   d
        #                         ^       ^
        #                         |       |
        #                     left    right
        #         # case 2: seen[a] = 0,which means a not in current window s[3:5] , since seen[a] = 0 < left = 3
        #         # we can keep moving right pointer.

        # seen = {}
        # l = 0
        # output = 0
        # for r in range(len(s)):
        #     # """
        #     # If s[r] not in seen, we can keep increasing the window size by moving right pointer
        #     # """
        #     if s[r] not in seen:
        #         output = max(output, r-l+1)
        #     # """
        #     # There are two cases if s[r] in seen:
        #     # case1: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
        #     # case2: s[r] is not inside the current window, we can keep increase the window
        #     # """
        #     else:
        #         if seen[s[r]] < l:
        #             output = max(output, r-l+1)
        #         else:
        #             l = seen[s[r]] + 1
        #     seen[s[r]] = r

        # return output

        charSet = set()
        # left sliding window
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                # remove repeating character
                charSet.remove(s[l])
                l += 1
            # add to set
            charSet.add(s[r])
            # current res = r-l+1
            res = max(res, r - l + 1)

        return res