class Solution:
    # not work
    # def restoreIpAddresses(self, s: str) -> List[str]:
    #     if len(s) < 4 or len(s) > 12:
    #         return []

    #     if len(s) == 4:
    #         return [".".join(list(s))]

    #     res = []
    #     if len(s) == 12:
    #         for i in range(4):
    #             if int(s[i * 3:i * 3 + 3]) < 0 or int(s[i * 3:i * 3 + 3]) > 255:
    #                 return res
    #             else:
    #                 res.append(s[i * 3:i * 3 + 3])

    #         return ".".join(res)

    # 回溯
    # 由于我们需要找出所有可能复原出的 IP 地址，因此可以考虑使用回溯的方法，对所有可能的字符串分隔方式进行搜索，并筛选出满足要求的作为答案。
    # 用递归函数 dfs(segId,segStart) 表示我们正在从 s[segStart] 的位置开始，搜索 IP 地址中的第 segId 段，其中 segId∈{0,1,2,3}
    # 从 segStart 开始，从小到大依次枚举当前这一段 IP 地址的结束位置 segEnd。如果满足要求，就递归地进行下一段搜索，调用递归函数 dfs(segId+1,segEnd+1)
    # 如果 s[segStart] 等于字符 0，那么 IP 地址的第 segId 段只能为 0
    # 如果提前遍历完了整个字符串，那么我们需要结束搜索，回溯到上一步

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/restore-ip-addresses/solutions/366426/fu-yuan-ipdi-zhi-by-leetcode-solution/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    def restoreIpAddresses(self, s: str) -> List[str]:
        SEG_COUNT = 4
        ans = list()
        segments = [0] * SEG_COUNT

        def dfs(segId: int, segStart: int):
            # 如果找到了 4 段 IP 地址并且遍历完了字符串，那么就是一种答案
            if segId == SEG_COUNT:
                if segStart == len(s):
                    ipAddr = ".".join(str(seg) for seg in segments)
                    ans.append(ipAddr)
                return

            # 如果还没有找到 4 段 IP 地址就已经遍历完了字符串，那么提前回溯
            if segStart == len(s):
                return

            # 由于不能有前导零，如果当前数字为 0，那么这一段 IP 地址只能为 0
            if s[segStart] == "0":
                segments[segId] = 0
                dfs(segId + 1, segStart + 1)
                return

            # 一般情况，枚举每一种可能性并递归
            addr = 0
            for segEnd in range(segStart, len(s)):
                addr = addr * 10 + (ord(s[segEnd]) - ord("0"))
                if 0 < addr <= 0xFF:
                    segments[segId] = addr
                    dfs(segId + 1, segEnd + 1)
                else:
                    break

        dfs(0, 0)
        return ans

    # # 作者：力扣官方题解
    # # 链接：https://leetcode.cn/problems/restore-ip-addresses/solutions/366426/fu-yuan-ipdi-zhi-by-leetcode-solution/
    # # 来源：力扣（LeetCode）
    # # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 3 nested for loop
    def restoreIpAddresses(self, s: str) -> List[str]:
        l = len(s)
        if l > 12 or l < 4:
            return []

        arr = []
        for i in range(1, min(4, l - 2)):
            for j in range(i + 1, min(i + 4, l - 1)):
                for k in range(j + 1, min(j + 4, l)):
                    if l - k > 3:
                        continue
                    n = [s[:i], s[i:j], s[j:k], s[k:]]
                    flag = False
                    for c in n:
                        if c[0] == '0' and c != '0':
                            flag = True
                            break
                    if flag:
                        continue
                    # print(n)
                    a, b, c, d = map(int, n)
                    if 0 <= a <= 255 and 0 <= b <= 255 and 0 <= c <= 255 and 0 <= d <= 255:
                        arr.append(str(a) + '.' + str(b) + '.' + str(c) + '.' + str(d))
        return arr