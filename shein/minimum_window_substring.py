class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if len(s) < len(t):
        #     return ""

        # m, n = len(s), len(t)
        # min_str = s
        # l = 0
        # cur_str = ""

        # for r in range(m):

        # need, missing = collections.Counter(t), len(t)
        # i = start = end = 0
        # for j, c in enumerate(s, 1):
        #     missing -= need[c] > 0
        #     need[c] -= 1
        #     if not missing:
        #         while need[s[i]] < 0:
        #             need[s[i]] += 1
        #             i += 1
        #         if not end or j - i < end - start:
        #             start, end = i, j
        # return s[start:end]

        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        needCnt = len(t)

        i = 0
        res = (0, float('inf'))

        for j, c in enumerate(s):
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1
            if needCnt == 0:  # 步骤一：滑动窗口包含了所有T元素
                while True:  # 步骤二：增加i，排除多余元素
                    c = s[i]
                    if need[c] == 0:
                        break
                    need[c] += 1
                    i += 1
                if j - i < res[1] - res[0]:  # 记录结果
                    res = (i, j)
                need[s[i]] += 1  # 步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt += 1
                i += 1
        return '' if res[1] > len(s) else s[res[0]:res[1] + 1]  # 如果res始终没被更新过，代表无满足条件的结果

# 作者：Mcdull0921
# 链接：https://leetcode.cn/problems/minimum-window-substring/solution/tong-su-qie-xiang-xi-de-miao-shu-hua-dong-chuang-k/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。