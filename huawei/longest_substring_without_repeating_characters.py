class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # not work
        # if len(s) <= 1:
        #     return len(s)

        # max_len = 1

        # l, r = 0, 1
        # while r<len(s):
        #     if s[r] not in s[l:r]:
        #         max_len = max(max_len, r - l + 1)
        #     else:
        #         l = r
        #     r += 1

        # return max_len

        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/longest-substring-without-repeating-characters/solution/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetc-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。