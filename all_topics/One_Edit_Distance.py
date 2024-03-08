class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False

        n_s, n_t = len(s), len(t)

        # if (n_s == 0 or n_t == 0) and (abs(n_s - n_t) == 1):
        #     return True

        if n_s > n_t:
            s, t = t, s
            n_s, n_t = n_t, n_s

        # print(s, t, n_s, n_t)
        if n_s < n_t:
            for i in range(n_t):
                if i >= n_s:
                    if s + t[i] == t:
                        return True
                    else:
                        return False
                if s[i] == t[i]:
                    continue
                # print(s[:i] + t[i] + s[i:], t)
                if s[:i] + t[i] + s[i:] == t:

                    return True
                else:
                    return False

        else:
            for i in range(n_s):
                if s[i] == t[i]:
                    continue
                # print(s[:i] + t[i] + s[i + 1:], t)
                if s[:i] + t[i] + s[i + 1:] == t:

                    return True
                else:
                    return False

    # 一次遍历算法
    # 如果长度差了2个或更多字符，那么 s 和 t 就不可能是一次编辑之差的字符串
    # 假设 s 的长度总是短于或等于 t 的长度
    def isOneEditDistance(self, s: 'str', t: 'str') -> 'bool':
       ns, nt = len(s), len(t)

       # 确保 s 比 t 短。
       if ns > nt:
           return self.isOneEditDistance(t, s)

       # 如果长度差异大于 1，则字符串不是一个编辑距离。
       if nt - ns > 1:
           return False

       for i in range(ns):
           if s[i] != t[i]:
               # 如果字符串具有相同的长度
               if ns == nt:
                   return s[i + 1:] == t[i + 1:]
               # 如果字符串具有不同的长度
               else:
                   return s[i:] == t[i + 1:]

       # 如果在 ns 距离上没有差异，则仅当 t 有多一个字符时，字符串才有一次编辑。
       return ns + 1 == nt

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/one-edit-distance/solutions/1486105/xiang-ge-wei-1-de-bian-ji-ju-chi-by-leet-8bu4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。