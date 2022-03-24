class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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
            res = max(res, r-l+1)

        return res