# import re


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # matched = ""

        # strs = sorted(strs, key=len)

        # for i in range(len(strs[0])):
        #     for j in strs[1:]:
        #         if (not re.search("^" + strs[0][:i+1], j)):
        #             return matched
        #     matched += strs[0][i]

        # return matched

        res = ""
        # *: unpack list into element
        # res = [['a', 'b', 'c'], [1, 2, 3]]
        # zip(*res)
        # this is the same as calling zip(['a', 'b', 'c'], [1, 2, 3])
        for a in zip(*strs):
            if len(set(a)) == 1:
                res += a[0]
            else:
                return res
        return res
